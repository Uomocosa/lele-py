import builtins
from types import ModuleType

def isinstance(obj, class_or_tuple):
    """
    Shadows the built-in isinstance.
    1. Tries standard isinstance.
    2. If that fails because 'class_or_tuple' is a Module, 
       it looks for a class inside that module with the same name.
    """
    try:
        return builtins.isinstance(obj, class_or_tuple)
    except TypeError:
        if builtins.isinstance(class_or_tuple, ModuleType):
            name = class_or_tuple.__name__.split('.')[-1]
            if hasattr(class_or_tuple, name):
                real_class = getattr(class_or_tuple, name)
                return builtins.isinstance(obj, real_class)
        raise
