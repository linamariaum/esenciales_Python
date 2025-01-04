class PerroF:
    def pasear(self):
        print("Paseando")

    def comer(self):
        print("Comiendo")

class GatoF:
    def comer(self):
        print("Comiendo")
    
    def maullar(self):
        print("maullando")

# Para crear la herencia:
#Al una clase heredar de otra toma todos sus metodos y propiedades de clase

class Animal:
    def comer(self):
        print("Comiendo")

    def dormir(self):
        print("Durmiendo animal")

class Perro(Animal):
    def pasear(self):
        print("Paseando")

class Gato(Animal):    
    def maullar(self):
        print("Maullando")

class Lupita(Gato): # Herencia multinivel
    def jugar(self):
        print("Durmiendo")

class Pez:
    def nadar(self):
        print("Nadando")

    def dormir(self):
        print("Durmiendo pez")

class Ballena(Animal, Pez): # Herencia multiple
    #Hereda de dos clases distintas donde ambas contienen un metodo igual, así que sobreescribe el metodo por el de la primera clase en el orden de herencia en la deficion de esta clase Ballena
    def onda(self):
        print("Enviando onda")

class Ave:
    def __init__(self):
        self.volador = "volador"

    def vuela(self):
        print("Volando ave")

class Pato(Ave):
    #Hereda de una clase que contiene un mismo metodo de esta propia clase por lo que anula el metodo de la clase padre y conserve el metodo propio
    
    def __init__(self):
        self.nadador = "nadador"
    
    def vuela(self):
        print("Volando pato")

class Garza(Ave):
    def __init__(self):
        super().__init__()
        self.cazador = "cazador"

    def vuela(self):
        super().vuela() # Super da acceso a los metodos del padre
        print("Volando garza")


gato = Gato()
gato.maullar()
gato.comer()
lupita = Lupita() # Herencia multinivel, solo se sugiere a nivel 2 no más
lupita.jugar()
lupita.maullar()
lupita.comer()

ballena = Ballena()
ballena.onda()
ballena.nadar()
ballena.comer()
ballena.dormir() # Saca el de Animal por el orden en el que esta heredando la clase, tratar de que las clases no tengan metodos iguales que hereden

pato = Pato()
pato.vuela() # Saca la implementacion del metodo propio (subclase), anulando el heredado
garza = Garza()
garza.vuela() # Saca la implementacion del metodo heredado y del metodo propio (subclase)
#print(pato.volador, pato.nadador) # Error, Pato no contiene el atributo volador (ya que su init no llamo al init del padre, por tanto la propiedad no existe)
print(garza.volador, garza.cazador)
