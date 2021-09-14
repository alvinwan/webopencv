from .aio import app
from . import transforms


class App:
    def __init__(self):
        self.app = app

    def transform(self, name):
        """Register a new transformation for the video stream."""
        def decorator(transform):
            transforms.add_transform(name, transform)
            return transform
        return decorator

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)