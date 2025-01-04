mensaje = "Hola mundo"
print(type(mensaje))

class Perro:
    patas = 4 # Propiedades de clase
    def __init__(self, nombre, raza, edad): #Constructor
        self.__raza = raza ## propiedad privada, solo se puede acceder dentro de la clase
        self.edad = edad ## pasará por su setter por los decoradores de las notaciones para realizar validaciones
        self.nombre = nombre ## propiedad publica, se puede hacer referencia tanto dentro de la clase como desde la instancia
        #print(self.nombre, self.__raza, self.__edad)

    def get_raza(self):
        return self.__raza

    def set_raza(self, raza):
        self.__raza = raza

#Estos dos metodos quedan completamente ocultos y el constructor es capaz automaticamente de invocar este setter antes de construir el obj
# pero no pueden ser llamados desde las instancias
    @property # Esta notacion es para los getter y a su vez esta notacion crea una notacion con el nombre de este metodo
    def edad(self): # Esto es más elegante y asi no tener que crear los metodos get_edad() y su set para los atributos de la clase
        print("pasando por getter edad")
        return self.__edad ## propiedad privada, solo se puede acceder dentro de la clase

    @edad.setter # Aqui se usa la notacion edad creada por el decorador property de arriba y se le indica que es un setter
    def edad(self, edad):
        print("pasando por setter edad")
        if edad.strip():
            self.__edad = edad
        return

    def __mi_metodo_privado(self):
        print("Exclusivo para uso interno")

    def habla(self):
        print("Wow")
    
    def juega(self):
        self.__mi_metodo_privado()
        print(f" {self.nombre} esta jugando")

    @classmethod # metodo de clase
    def saluda(cls):
        print("Saludando")

    @classmethod # metodo de clase y metodo de fabrica
    def factory(cls):
        return cls("Toby", "Fresh", "2")

    # Las clases tienen metodos magicos, todos disponibles por herencia de class en Python
    # Todos inician con __metodo__ y no se invocan, se llaman de forma indirecta por ejm el __init__ la instancia no lo invoca directamente pero __init__ si se ejecuta al crear una instancia

    def __str__(self):
        return f"Clase Perro: {self.nombre}"
    
    def __del__(self): # Destructor
        print(f"Chao perro {self.nombre}")

    def __eq__(self, otroObj): # Define la comparacion de igualdad
        return self.nombre == otroObj.nombre and self.edad == otroObj.edad and self.__raza == otroObj.get_raza()

    ## Si se define el metodo magico de eq, este metodo magico de ne no es necesario ya que Python lo infiere
    def __ne__(self, otroObj): # Define la comparacion de desigualdad
        return self.nombre != otroObj.nombre or self.edad != otroObj.edad or self.__raza != otroObj.get_raza()
    
    def __lt__(self, otroObj): # menor que (al definir este python infiere cual es el mayor que __gt__)
        return self.nombre < otroObj.nombre
    # __gt__  mayor que
    # __le__  menor igual que
    # __ge__  mayor igual que

print(Perro.patas)
Perro.saluda()
mi_perro = Perro("Chanchito", "Labrador", "2")
mi_perro2 = Perro("Chanchi", "Hosky", "2")
mi_perro3 = Perro.factory()
print(mi_perro3.nombre)
mi_perro.saluda()
Perro.patas = 3
print(Perro.patas)
print(mi_perro.patas)
print(mi_perro2.patas)
mi_perro2.patas = 7
print(Perro.patas)
print(mi_perro.patas)
print(mi_perro2.patas)
print(type(mi_perro))
mi_perro.habla()
mi_perro.juega()
print(Perro.patas)
print(isinstance(mi_perro, Perro))

##mi_perro.__raza = "Mestizo"
#print(mi_perro.__raza) # Error no se puede acceder a la propiedad
print(mi_perro.__dict__) # no se debe acceder asi
print(mi_perro._Perro__raza) # no se debe acceder asi

print(mi_perro.get_raza()) # acceder a propiedades privadas mediandte un get
#mi_perro.__mi_metodo_privado() # Error por privado
#Perro.__mi_metodo_privado() # Error por privado

print(mi_perro) # Saca el espacio en memoria, cuando no esta implementado el metodo magico de str

#perro_validaciones = Perro(True, 3, False) # Aunque tipado, deja crear una instancia así
#perro_validaciones = Perro(True, 3, False) # Pero si lo ejecuto asi, despues de crearle los decorradores de property para la validacion de data, entonces esta creacion saca error
perro_validaciones = Perro(True, 3, "8") # Asi ya queda validado el obj
print(perro_validaciones.nombre)
#perro_validaciones.edad() # Error no se puede acceder
print(perro_validaciones.edad)

print(mi_perro) # Saca lo especificado en el metodo magico str, despues de este ser implementado en la clase
texto = str(mi_perro) # Gracias a la implementacion del metodo magico str, la instancia se transforma en un string
print(texto)
# Mas informacion sobre los metodos magicos de python en: https://rszalski.github.io/magicmethods/#representations
# Se invoca al metodo magico destructor así (este debe estar previamente implementado en la clase):
del mi_perro3

### Comparaciones entre objetos
print("Comparaciones")
perrito1 = Perro("Tobias", "Labrador", "3")
perrito2 = Perro("Tobias", "Labrador", "3")
print(perrito1 == perrito2) # Saca False porque son dos instancias distintas con dos posiciones en memoria
print(perrito1 == perrito2) # Saca True despues de implementado el metodo magico __eq__ ya que con este se le indica como realizar la comparacion de igualdad
print(perrito1 != perrito2) # Saca False despues de implementado el metodo magico __ne__ ya que con este se le indica como realizar la comparacion de desigualdad
print(perrito1 < perrito2)
