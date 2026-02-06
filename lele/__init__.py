import new_import_system
new_import_system.install(__file__)

# Simpler exports/imports:
import lele
P = lele.Path.P # for example you can call it via lele.P instead of lele.Path.P
isinstance = lele.Metaprogramming.isinstance
type = lele.Metaprogramming.get_type_from_lazy_module
