import new_import_system
new_import_system.install(__file__)

# Simpler exports/imports:
from . import Path as _Path
from . import Metaprogramming as _Metaprogramming
import lele
P = _Path.P # for example you can call it via lele.P instead of lele.Path.P
isinstance = _Metaprogramming.isinstance
type = _Metaprogramming.get_type_from_lazy_module
