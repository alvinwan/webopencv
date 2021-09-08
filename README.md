# webopencv &middot; [demo](webopencv.glitch.me) &middot; [1-click setup](https://glitch.com/edit/#!/remix/webopencv)
Using WebRTC, stream live video feed from a webpage to a server-side OpenCV Python script. This is primarily written for educational purposes, **giving students the ability to work with a webcam, without installing anything on their computers**. Most importantly, this library enables larger-scale, remote computer vision courses to make use of the webcam via a 1-click WebOpenCV setup.

🎥 Live demo: [webopencv.glitch.me](https://webopencv.glitch.me)

👉 1-click WebOpenCV Setup: [Fork on Glitch](https://glitch.com/edit/#!/remix/webopencv)

created by [Alvin Wan](https://alvinwan.com)

## Why Use WebOpenCV?

This sidesteps a major issue with most computer vision tutorials that make use of the webcam:

1. Installing the necessary Python packages is painful for select platforms and packages.
2. Webcam access from Python is finicky.

This library addresses both concerns by launching a web server. This client webpage then receives webcam input, which is fed back to a server-side Python script. This approach allows you to

1. Automatically install Python packages on a service like [replit.com](https://replit.com) or [glitch.com](https://glitch.com). Students just access a website. No setup required on the student's computer.
2. Only requires well-established web-based video protocols. If your student's computer runs Google Meet, it'll run your `webopencv` project too.

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
