from .app import app

class App:
    def __init__(self, backend='flask'):
        self.app = app
        self.transforms = {}

    def transform(self, name):
        """Register a new transformation for the video stream."""
        def decorator(f):
            self.transforms[name] = f
            return f
        return decorator

    def run(self, *args, **kwargs):
        self.app.run()