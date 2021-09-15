# webopencv &middot; [demo](https://webopencv.glitch.me) &middot; [1-click setup](https://glitch.com/edit/#!/remix/webopencv)
Stream webcam from a webpage to a server-side OpenCV Python script. This **gives you the ability to work with a webcam in Python, without installing anything on your computer**.

🎥 Live demo: [webopencv.glitch.me](https://webopencv.glitch.me)

👉 1-click WebOpenCV Setup: [Fork on Glitch](https://glitch.com/edit/#!/remix/webopencv)

💻 View demo source: [on Glitch](https://glitch.com/edit/#!/webopencv) or [on Github](https://github.com/alvinwan/webopencv/tree/main/demo)

created by [Alvin Wan](https://alvinwan.com), for an online computer vision tutorial

## Why Use WebOpenCV?

WebOpenCV makes it easy for anyone to start working with their own webcam, in Python. Before WebOpenCV, you would need to (1) install packages, their package managers, and miscellaneous tools *on your own computer*, then (2) pray that webcam access worked. Now, you simply click once to launch a free, remote server that comes pre-setup. No installation on your own computer necessary.

## Getting Started

**For the 1-click WebOpenCV setup, [fork on Glitch](https://glitch.com/edit/#!/remix/webopencv).**

Alternatively, to setup locally on your machine instead, install the Python package.

```bash
pip install webopencv
```

Create a new file `app.py`.

```python
import webopencv as wcv

app = wcv.WebApplication()

@app.transform('Hello')
def helloworld(img, frame):
    return img

if __name__ == '__main__':
    app.run()
```

Then, run the file.

```bash
python app.py
```

This launches a web server by default at `https://localhost:8080`. Navigate to that URL, and hit "Start" to see the demo in action. Note: When developing locally, navigating to `https://0.0.0.0:8080` won't work. Make sure to use `localhost`.

## Transforms

Create *transforms*, or hooks that process images in a real-time video feed. Each transform takes in an

1. `img`: numpy array image
2. `frame`: `VideoFrame` object that additionally contains metadata, like time

Like with Flask routes, you can register transforms using a decorator. Add whatever processing you would like to the transform, and return the image at the end. For example, the below adds a "cinematic" crop to the live feed, by adding black bars.

```python
@app.transform('Cinematic')
def cinematic(img, frame):
    h, w, _ = img.shape
    img[-w//4:] = 0
    img[:w//4] = 0
```

**Default Transform**: Use `default=True` in the `transform` decorator to set a transform as the default on page load. Note that only 1 transform can be set as default. If no transform has `default=True` set, the default is no transform on page load.

## Customize Homepage

To build a custom homepage:

1. Initialize the app *without* the default homepage. You can use either the `aiohttp` or `Flask` backends.
2. Add your own homepage with:
    - WebOpenCV's client-side Javascript: `<script src="/client.js"></script>`
    - a `video` tag with `id="video"`, for the webcam feed: `<video id="video" autoplay="true" playsinline="true"></video>`
    - a `button` tag with `id="action"`, for "Start" and "Stop": `<button id="action"></button>` 

**aiohttp**: The default backend uses `aiohttp`, so you can treat `app` as you would any other `web.Application` object.

```python
from aiohttp import web
import webopencv as wcv

app = wcv.WebApplication(use_default_homepage=False)

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
```

**Flask**: You can alternatively use the Flask backend, treating the `app` as you would any other `Flask` object. *Note that the Flask implementation drops the ICE connection. Needs debugging.*

```python
import webopencv as wcv

app = wcv.Flask(use_default_homepage=False)

@app.route("/")
def index():
    return """
    <html>
        Custom webpage
        <button id="action"></button>
        <video id="video" autoplay="true" playsinline="true"></video>
        <script src="/client.js"></script>
    </html>
    """

if __name__ == '__main__':
    app.run()
```

*Acknowledgments: This library was built off of the `aiortc` official server example.*
