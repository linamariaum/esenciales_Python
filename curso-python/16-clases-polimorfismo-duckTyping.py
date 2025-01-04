from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass

class Usuario(Model):
    def guardar(self):
        print("Guardando en BD")

class Sesion(Model):
    def guardar(self):
        print("Guardando en Archivo")


def guardar(entidad):
        entidad.guardar()

def guardarPro(entidades):
    for entidad in entidades:
        entidad.guardar()

usuario = Usuario()
guardar(usuario)
sesion = Sesion()
guardar(sesion)

# Polimorfismo, varios objetos con una interfaz similar y luego guardar es capaz de llamar el guardar de cada uno sin tener que especificarlo
# Implementaciones distinta para el mismo objetivo en distintos tipos de objetos
guardarPro([sesion, usuario]) # Esto es polimorfismo


## Duck typing
# Python tiene tipado dinamico asi que no va a validar si mis dos objs extienden del mismo obj Model
# La unica condicion para que la ejecucion no se rompa es que lo que entre al metodo guardarPro generico, contenga su propio metodo guardar, es decir
# Esto se conoce como Duck typing y significa "si camina como pato y suena como pato entonces es un pato"


class Ejm1:
    def guardar(self):
        print("Guardando en Ejemplo 1")

class Ejm2:
    def guardar(self):
        print("Guardando en Ejemplo 2")

ejemplo1 = Ejm1()
ejemplo2 = Ejm2()
guardarPro([ejemplo1, ejemplo2])
