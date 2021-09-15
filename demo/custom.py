from aiohttp import web
import webopencv as wcv

app = wcv.WebApplication(use_default_homepage=False, framerate=5)

html = """
<html>
    Custom webpage
    <button id="action"></button>
    <video id="video" autoplay="true" playsinline="true"></video>
    <script src="/client.js"></script>
</html>
"""

def index(app):
    return web.Response(text=html, content_type="text/html")

if __name__ == '__main__':
    app.router.add_get_url('/', index)
    app.run()