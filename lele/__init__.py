import new_import_system
new_import_system.install(__file__)

import importlib
P = importlib.import_module("lele.Path.P")
type = importlib.import_module("lele.Metaprogramming.get_type_from_lazy_module")
isinstance = importlib.import_module("lele.Metaprogramming.isinstance")

def test_():
    print(P("."))
