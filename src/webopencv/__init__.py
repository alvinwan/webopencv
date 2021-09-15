from . import aio, flsk, transforms


class Base:
    def transform(self, name):
        """Register a new transformation for the video stream."""
        def decorator(transform):
            transforms.add_transform(name, transform)
            return transform
        return decorator


class WebApplication(Base, aio.App):
    pass


class Flask(Base, flsk.App):
    pass