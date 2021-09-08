# webopencv &middot; [demo](https://webopencv.glitch.me) &middot; [1-click setup](https://glitch.com/edit/#!/remix/webopencv)
Stream webcam from a webpage to a server-side OpenCV Python script. This **gives you the ability to work with a webcam in Python, without installing anything on your computer**. All it takes is 1 click to demo or spin up an editable copy.

🎥 Live demo: [webopencv.glitch.me](https://webopencv.glitch.me)

👉 1-click WebOpenCV Setup: [Fork on Glitch](https://glitch.com/edit/#!/remix/webopencv)

created by [Alvin Wan](https://alvinwan.com), originally for a larger-scale, online computer vision tutorial

## Why Use WebOpenCV?

This sidesteps a major issue with most computer vision tutorials that make use of the webcam:

1. Installing the necessary Python packages is painful for select platforms and packages.
2. Webcam access from Python is finicky.

This library addresses both concerns by launching a web server. This client webpage then receives webcam input, which is fed back to a server-side Python script. This approach allows you to

1. Setup a free, remote instance via [glitch.com](https://glitch.com) just by clicking on a link. No computer setup necessary.
2. Only requires well-established web-based camera access. If your computer runs Google Meet, you can use this.

This library is effectively the [demo from `aiortc`](https://github.com/aiortc/aiortc/tree/main/examples/server), except with a few niceties that (1) make it easy for any student to get started, with a few lines of code and (2) some connector code that minimizes the difference between `cv2` and its online cousin (this package), `wcv2`.

## Getting Started

For the 1-click WebOpenCV setup, [fork on Glitch](https://glitch.com/edit/#!/remix/webopencv).

Alternatively, to setup locally on your machine instead, install the Python package.

```
pip install webopencv
```

Create a new file `app.py`.

```
from aiohttp import web
from wcv2 import app


if __name__ == '__main__':
    web.run_app(
        app.get_web_app(),
        port=8000
    )
```

Then, run the file.

```
python app.py
```
