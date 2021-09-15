"""aiohttp-powered web application backend"""

from aiohttp import web
from .app import on_offer, on_shutdown
from .utils import ROOT

import json
import os


def get_static_resource(path, **kwargs):
    content = open(os.path.join(ROOT, path), "r").read()
    return web.Response(text=content, **kwargs)


async def index(request):
    return get_static_resource("templates/index.html", content_type="text/html")


async def javascript(request):
    return get_static_resource("static/client.js", content_type="application/javascript")


async def offer(request):
    params = await request.json()
    pc = await on_offer(params, sender=request.remote)
    return web.Response(
        content_type="application/json",
        text=json.dumps(
            {"sdp": pc.localDescription.sdp, "type": pc.localDescription.type}
        ),
    )


class App(web.Application):

    def __init__(self):
        super().__init__()
        self.on_shutdown.append(on_shutdown)
        self.router.add_get("/", index)
        self.router.add_get("/client.js", javascript)
        self.router.add_post("/offer", offer)

    def run(self, *args, **kwargs):
        """Light wrapper around aiohttp.web.run_app"""
        return web.run_app(self, *args, **kwargs)
