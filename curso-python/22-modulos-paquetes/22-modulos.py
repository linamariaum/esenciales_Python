# Cuando importamos modulos Python automaticamente crea la carpeta __pyche__ con los modulos en que importamos compilados en bycode
# Esto es para mejorar el rendimiento de carga de modulos

# Un modulo es cuando nos traemos la importacion de la funcionalidad perteneciente en otro archivo a este archivo

# Import un modulo
from usuario_impuestos import guardar, pagar_impuestos

guardar()
pagar_impuestos()

print(__name__)
