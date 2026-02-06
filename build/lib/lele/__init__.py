import new_import_system
new_import_system.install(__file__)

import lele
print(lele)
P = lele.Path.P
print(P)
from lele.Metaprogramming import isinstance # bad idea ;; context switching
from lele.Metaprogramming import get_type_from_lazy_module as type # bad idea ;; context switching
