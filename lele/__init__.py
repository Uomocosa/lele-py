import new_import_system
new_import_system.install(__file__)

# Define what happens when someone accesses an attribute of lele
def __getattr__(name):
    if name == "P":
        from . import Path
        return Path.P
    
    if name == "isinstance":
        from . import Metaprogramming
        return Metaprogramming.isinstance
        
    if name == "type":
        from . import Metaprogramming
        return Metaprogramming.get_type_from_lazy_module

    raise AttributeError(f"module {__name__} has no attribute {name}")

# This tells IDEs/Static Analyzers that these variables exist
__all__ = ["P", "isinstance", "type"]
