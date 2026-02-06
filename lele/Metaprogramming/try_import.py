import importlib
from types import ModuleType
from typing import Optional

def try_import(module_name: str) -> Optional[ModuleType]:
    try:
        # This returns the module object itself
        return importlib.import_module(module_name)
    except (ImportError, ModuleNotFoundError):
        return None

def test_():
    lele = try_import("lele")
    nothing = try_import("non_existing_module")
    assert lele, f"lele NOT found!"
    assert nothing is None, f"Found nothing! HOW?"
