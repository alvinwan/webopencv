from aiohttp import web
from wcv2 import app


if __name__ == '__main__':
    web.run_app(
        app.get_web_app(),
        port=8000
    )