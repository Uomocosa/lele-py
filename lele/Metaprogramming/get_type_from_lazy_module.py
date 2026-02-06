import inspect
from types import ModuleType
from typing import Type, Any

def get_type_from_lazy_module(obj: ModuleType | Type[Any]) -> Type[Any]:
    """
    Resolves a class from a module if a module is passed.
    
    If 'obj' is a Module (e.g., lele.Dataset.Config), this function tries to 
    find a class inside it with the same name (lele.Dataset.Config.Config).
    
    If 'obj' is already a Class, it is returned as is.
    
    Args:
        obj: A python module or a class.
        
    Returns:
        The resolved Class type.
        
    Raises:
        AttributeError: If the module does not contain a class with the same name.
    """
    
    if inspect.ismodule(obj):
        module_name = obj.__name__.split('.')[-1]
        if hasattr(obj, module_name):
            potential_class = getattr(obj, module_name)
            if inspect.isclass(potential_class):
                return potential_class
        raise AttributeError(
            f"Module '{obj.__name__}' does not contain a class named '{module_name}'. "
            f"Please ensure the class name matches the file name (e.g. class Config inside Config.py)."
        )
    
    if inspect.isclass(obj):
        return obj
        
    return type(obj)
    # raise TypeError(f"Expected a Module or a Class, got {type(obj)}")


def test_():
    import lele
    print(lele.Metaprogramming.CSV_Logger)
    print(get_type_from_lazy_module(lele.Metaprogramming.CSV_Logger))
