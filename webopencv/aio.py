"""aiohttp-powered web application backend"""

from aiohttp import web
from jinja2 import Environment, PackageLoader, select_autoescape

from .app import on_offer, on_shutdown
from .utils import ROOT
from . import transforms

import json
import os


jinja = Environment(
    loader=PackageLoader("webopencv", ROOT),
    autoescape=select_autoescape()
)

def render_template(path, **kwargs):
    template = jinja.get_template(path)
    return template.render(
        **kwargs,
        get_transform=transforms.get_transform,
        transforms=transforms.get_transform_ids(),
        get_default_transform_id=transforms.get_default_transform_id,
    )


def get_index(**kwargs):
    async def index(request):
        content = render_template("templates/index.html", **kwargs)
        return web.Response(text=content, content_type="text/html")
    return index


def get_javascript(**kwargs):
    async def javascript(request):
        content = render_template("static/client.js", **kwargs)
        return web.Response(text=content, content_type="application/javascript")
    return javascript


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

    def __init__(self, use_default_homepage=True, framerate=15):
        super().__init__()
        self.on_shutdown.append(on_shutdown)
        self.router.add_get("/client.js", get_javascript(framerate=framerate))
        self.router.add_post("/offer", offer)

        if use_default_homepage:
            self.router.add_get("/", get_index(title="WebOpenCV Demo"))

    def run(self, *args, **kwargs):
        """Light wrapper around aiohttp.web.run_app"""
        return web.run_app(self, *args, **kwargs)
