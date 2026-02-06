import functools

def defined_in(impl_class):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            # Find the method with the same name on the implementation class
            impl_method = getattr(impl_class, func.__name__)
            # Call it with (self, *args, **kwargs)
            return impl_method(self, *args, **kwargs)
        return wrapper
    return decorator


def test_():
    """
    In a class, youll define a method like:

    @dataclass
    class Canvas:
        @defined_in(Excalidraw.CanvasMethod)
        def add_rectangle(self, x: int, y: int, width: int, height: int, color="#000000"):
            pass  
    
        @defined_in(Excalidraw.CanvasMethod)
        def add_image(self, file_path: str, x: int, y: int, width: Optional[int] = None):
            pass
    """
    pass
