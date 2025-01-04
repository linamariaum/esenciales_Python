from abc import ABC, abstractmethod
# abc: Abstract class

# Esta clase Model se podrá utilizar en todas las clases que esten apuntando a una tabla especifica de base de datos
class ModelF():
    # A como esta creada esta clase, se podrían crear directamente instancias de la clase Model y empezar a usar sus metodos :(
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("Error, tienes que definir una tabla")

    def guardar(self):
        print(f"Guardando {self.tabla} en BD")

    @classmethod
    def buscar_por_id(self, _id): # id es una palabra reservada de python, por lo que nuestra variable se llamara _id
        print(f"Buscando por id {_id} en BD en la tabla {self.tabla}")


class Usuario(ModelF):
    # Al heredar de ModelF no esta obligada esta subclase a tener la propiedad tabla, pero sin esta propiedad no funcionaria la logica que deseamos :(
    tabla = "Usuario"


class ModelMejorada(ABC):
    # Ahora esta clase es abstracta y con los decoradores se le indica Si o Si cuales propiedades o metodos Deben ser creados en las subclases que hereden de esta clase
    #def __init__(self): # Ya no se necesita constructor, esta clase no se puede instanciar

    @property #indica que es una propiedad y no un metodo
    @abstractmethod # esta propiedad tambien se puede utilizar en los metodos para que obligatoriamente la subclase los implemente
    def tabla(self): # Al esta propiedad ser abstracta se TIENE que definir en la subclase que herede de esta clase
        pass

    def guardar(self):
        print(f"Guardando {self.tabla} en BD")

    @abstractmethod
    def pintar(self):
        pass

    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando por id {_id} en BD en la tabla {self.tabla}")

class UsuarioMejorado(ModelMejorada):
    # Al heredar de ModelMejorado que es abstracta y que especifica cual metodo es abstracto
    #  entonces esta obligada esta subclase a tener la implementacion de tabla :)
    tabla = "UsuarioMejorado" # TIENE que tener la implementacion de esta propiedad por tener el decorador @abstractmethod

    def pintar(self): # TIENE que tener la implementacion de este metodo por tener el decorador @abstractmethod
        print("Pintando")


usuario = Usuario()
usuario.guardar()
usuario.buscar_por_id(123) #De esto no deberia encargarse la instancia sino la clase, así que colocaremos el decorador en el metodo
Usuario.buscar_por_id(123)
#Usuario.guardar() # Error, ya que guardar no es un metodo con el decorador de classmethod

modelF = ModelF() # Me permite crear instancia de la clase, pero no tiene sentido para nuestra logica :(
ModelF.buscar_por_id(456)
#model = ModelMejorada() # Error, no se puede instanciar la clase abstracta, esto es lo que buscamos :)

usuarioMejorado = UsuarioMejorado()
