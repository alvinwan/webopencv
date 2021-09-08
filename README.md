# webopencv
Using WebRTC, stream live video feed from a webpage to a server-side OpenCV Python script. This is primarily written for educational purposes, **giving students the ability to work with a webcam, without installing anything on their computers**. Most importantly, this library enables larger-scale, remote computer vision courses that make use of the webcam.

This sidesteps a major issue with most computer vision tutorials that make use of the webcam: (1) Installing the necessary Python packages is a major barrier. (2) Webcam access from Python is finicky at best. This library addresses both concerns by launching a web server. This client webpage then receives webcam input, which is fed back to a server-side Python script. This approach allows you to (1) automatically install Python packages on a service like [replit.com](https://replit.com) or [glitch.com](https://glitch.com) and (2) only requires well-established web-based video protocols. If your student's computer runs Google Meet, it'll run your `webopencv` project too.

This library is effectively the [demo from `aiortc`](https://github.com/aiortc/aiortc/tree/main/examples/server), except with a few niceties that (1) make it easy for any student to get started, with a few lines of code and (2) some connector code that minimizes the difference between `cv2` and its online cousin (this package), `wcv2`.

## Getting Started

**100% Remote Setup**: View the live demo at [webopencv.glitch.me](https://webopencv.glitch.me). To get started with the code, simply [fork the webopencv Glitch project](https://glitch.com/edit/#!/remix/vr101-nature-step2-starter).

**Local Setup**: To setup locally on your machine instead, install the Python package.

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