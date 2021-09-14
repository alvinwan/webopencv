from .app import app
from .transforms import add_transform

class App:
    def __init__(self):
        self.app = app
        self.transforms = {}

    def transform(self, name):
        """Register a new transformation for the video stream."""
        def decorator(transform):
            add_transform(name, transform)
            return transform
        return decorator

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)