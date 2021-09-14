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

The library mainly exists to provide a few niceties that (1) make it easy for any student to get started, with a few lines of code and (2) make it easy to try `cv2` manipulations on a live feed.

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

Like with Flask routes, you can register transforms using a decorator. Add whatever processing you would like to the transform, and return the image at the end. For example, the below adds a "cinematic" crop to the live feed.

```python
@app.transform('Cinematic')
def cinematic(img, frame):
    h, w, _ = img.shape
    img[-w//4:] = 0
    img[:w//4] = 0
```

Acknowledgments: The core logic is borrowed from the `aiortc` official server example.
