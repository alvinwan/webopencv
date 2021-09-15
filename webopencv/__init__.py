from . import aio, flsk, transforms


class Base:
    def transform(self, name, default=False):
        """Register a new transformation for the video stream."""
        def decorator(transform):
            transforms.add_transform(name, transform)
            if default:
                transforms.set_default_transform(name)
            return transform
        return decorator


class WebApplication(Base, aio.App):
    pass


class Flask(Base, flsk.App):
    pass