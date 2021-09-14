# webopencv &middot; [demo](https://webopencv.glitch.me) &middot; [1-click setup](https://glitch.com/edit/#!/remix/webopencv)
Stream webcam from a webpage to a server-side OpenCV Python script. This **gives you the ability to work with a webcam in Python, without installing anything on your computer**.

🎥 Live demo: [webopencv.glitch.me](https://webopencv.glitch.me)

👉 1-click WebOpenCV Setup: [Fork on Glitch](https://glitch.com/edit/#!/remix/webopencv)

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
import wcv2

app = wcv2.WebApplication()

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

This launches a web server by default at `https://localhost:8080`. Navigate to that URL, and hit "Start" to see the demo in action.

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

*Acknowledgments: This library was built off of the `aiortc` official server example.*
