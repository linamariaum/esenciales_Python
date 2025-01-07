# Import un modulo
from usuario_impuestos import guardar, pagar_impuestos

# Import un paquete.modulo o paquete completo
from usuarios.accionesUno import accion_guardar, accion_pagar_impuestos
##otra forma es
import usuarios.accionesUno
## y entonces para acceder a los metodos sería:
usuarios.accionesUno.accion_guardar()
###otra forma es
from usuarios import accionesUno
### y entonces para acceder a los metodos sería:
accionesUno.accion_guardar()

# Import del sub-paquete
from usuarios.acciones.accionesDos import accion_guardar_dos, accion_pagar_impuestos_dos

guardar()
pagar_impuestos()
accion_guardar()
accion_pagar_impuestos()
accion_guardar_dos()
accion_pagar_impuestos_dos()
