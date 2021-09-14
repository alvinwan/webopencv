from aiohttp import web
from .app import get_web_app


class VideoCapture:
    def __init__(self, on_image=None):
        self.app = get_web_app()
        self.on_image = on_image

    def launch(self):
        return web.run_app(
            get_web_app(),
            port=8000
        )
