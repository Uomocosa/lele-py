import new_import_system
new_import_system.install(__file__)

# Define what happens when someone accesses an attribute of lele
def __getattr__(name):
    import lele
    print(lele)
    print(dir(lele))
    print(lele.__file__)
    if name == "P": return lele.Path.P
    if name == "isinstance": return lele.isinstance
    if name == "type": return lele.type
    raise AttributeError(f"module {__name__} has no attribute {name}")

# This tells IDEs/Static Analyzers that these variables exist
__all__ = ["P", "isinstance", "type"]
