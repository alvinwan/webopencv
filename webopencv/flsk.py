"""Flask-powered web application backend

TODO(alvin): ICE connection state does not reached completed stage
"""

from flask import Flask, render_template, request, jsonify
from .app import on_offer, on_shutdown
from .utils import ROOT

import atexit
import os


DEFAULT_TEMPLATE_FOLDER = os.path.join(ROOT, "templates")
DEFAULT_STATIC_FOLDER = os.path.join(ROOT, "static")


def index():
    return render_template("index.html")


async def offer():
    params = request.json
    pc = await on_offer(params, sender="null")
    return jsonify({
        "sdp": pc.localDescription.sdp,
        "type": pc.localDescription.type
    })


class App(Flask):

    def __init__(
            self, *args,
            template_folder=DEFAULT_TEMPLATE_FOLDER,
            static_folder=DEFAULT_STATIC_FOLDER,
            static_url_path="",
            use_default_homepage=True,
            **kwargs
        ):
        super().__init__(
            *args,
            template_folder=template_folder,
            static_folder=static_folder,
            static_url_path=static_url_path,
            **kwargs
        )
        self.add_url_rule("/offer", view_func=offer, methods=["POST"])
        # atexit.register(on_shutdown)  # TODO: doesn't actually work, because atexit doesn't await

        if use_default_homepage:
            self.add_url_rule("/", view_func=index)