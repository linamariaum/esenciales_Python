# Los paquetes pueden tener nombre dinamicos
from personas.gestion.crud import guardar_persona

# invoca el print(__name__) del modulo crud pero no imprime "main" sino "personas.gestion.crud" ya se no se ejecuta directamente el script de alla, sino mediante este script

print(__name__)
print(__package__)
print(__file__)
