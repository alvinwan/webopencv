"""aiohttp-powered web application backend"""

from aiohttp import web
from aiortc import MediaStreamTrack, RTCPeerConnection, RTCSessionDescription
from av import VideoFrame
from . import transforms

import asyncio
import json
import logging
import os
import uuid


ROOT = os.path.dirname(__file__)
logger = logging.getLogger("pc")
pcs = set()


class VideoTransformTrack(MediaStreamTrack):
    """
    A video stream track that transforms frames from an another track.
    """

    kind = "video"

    def __init__(self, track, transform):
        super().__init__()  # don't forget this!
        self.track = track
        self.transform = transform

    async def recv(self):
        frame = await self.track.recv()
        
        if self.transform in transforms.get_transform_names():
            # convert from video frame to numpy array
            img = frame.to_ndarray(format="bgr24")

            # run image transformation
            transform = transforms.get_transform(self.transform)
            img = transform(img)

            # Write back to video frame, with timestamp
            new_frame = VideoFrame.from_ndarray(img, format="bgr24")
            new_frame.pts = frame.pts
            new_frame.time_base = frame.time_base
            return new_frame

        return frame


async def offer(request):
    params = await request.json()
    offer = RTCSessionDescription(sdp=params["sdp"], type=params["type"])

    pc = RTCPeerConnection()
    pc_id = "PeerConnection(%s)" % uuid.uuid4()
    pcs.add(pc)

    def log_info(msg, *args):
        logger.info(pc_id + " " + msg, *args)

    log_info("Created for %s", request.remote)

    @pc.on("datachannel")
    def on_datachannel(channel):
        @channel.on("message")
        def on_message(message):
            if isinstance(message, str) and message.startswith("ping"):
                channel.send("pong" + message[4:])

    @pc.on("iceconnectionstatechange")
    async def on_iceconnectionstatechange():
        log_info("ICE connection state is %s", pc.iceConnectionState)
        if pc.iceConnectionState == "failed":
            await pc.close()
            pcs.discard(pc)

    @pc.on("track")
    def on_track(track):
        log_info("Track %s received", track.kind)

        local_video = VideoTransformTrack(
            track, transform=params["video_transform"]
        )
        pc.addTrack(local_video)

        @track.on("ended")
        async def on_ended():
            log_info("Track %s ended", track.kind)

    # handle offer
    await pc.setRemoteDescription(offer)

    # send answer
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    return web.Response(
        content_type="application/json",
        text=json.dumps(
            {"sdp": pc.localDescription.sdp, "type": pc.localDescription.type}
        ),
    )


async def on_shutdown(app):
    # close peer connections
    coros = [pc.close() for pc in pcs]
    await asyncio.gather(*coros)
    pcs.clear()


def static(path, **kwargs):
    async def page(request):
        content = open(os.path.join(ROOT, path), "r").read()
        return web.Response(text=content, **kwargs)
    return page


class App(web.Application):

    def run(self, *args, **kwargs):
        """Light wrapper around aiohttp.web.run_app"""
        return web.run_app(self, *args, **kwargs)


app = App()
app.on_shutdown.append(on_shutdown)
app.router.add_get("/", static("static/index.html", content_type="text/html"))
app.router.add_get("/client.js", static("static/client.js", content_type="application/javascript"))
app.router.add_post("/offer", offer)