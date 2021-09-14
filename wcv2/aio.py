"""aiohttp-powered web application backend"""

from aiohttp import web
from aiortc import MediaStreamTrack, RTCPeerConnection, RTCSessionDescription
from av import VideoFrame
from .app import on_offer, on_shutdown
from . import transforms
from .utils import ROOT, logger

import asyncio
import json
import logging
import os
import uuid


async def offer(request):
    params = await request.json()
    pc = await on_offer(params, sender=request.remote)
    return web.Response(
        content_type="application/json",
        text=json.dumps(
            {"sdp": pc.localDescription.sdp, "type": pc.localDescription.type}
        ),
    )


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