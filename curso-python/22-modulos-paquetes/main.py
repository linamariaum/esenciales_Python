import personas.impuestos
from personas.impuestos.utilidades import pagar_impuestos_persona

pagar_impuestos_persona()

import personas
print(dir(personas))
print(personas.__name__)
print(personas.__package__)
print(personas.__path__)
print(personas.__file__)

print(personas.gestion.__name__)
print(personas.impuestos.__package__)
print(personas.gestion.__path__)
print(personas.gestion.__file__)
