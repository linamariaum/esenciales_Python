## Primera forma [Pero si el lugar de Correa deseo un arnes para el Perro, esta implementacion presenta problemas]
# import Correa

# class Perro:
#     def __init__(self):
#         self.correa = Correa()

## Otra forma
# class Perro:
#     def __init__(self, Correa):

#------------------------------------------------------------------------
# import usuario
# def guardarSinInyeccion():
#     usuario.guardar()

# La inyeccion de dependencias permite:
# - Reutilizar mas el codigo
# - Nos permite desacoplar el codigo para que este sea mas facil de reutilizar
# - Mas sencillo de probar mediantes Test
def guardarConInyeccion(entidad): # Funcionara la inyeccion siempre y cuando las entidades a inyectar posean los mismo metodos
    entidad.guardar()


#------------------------------------------------------------------------
# Inyeccion de dependencias utilizando Paths

from pathlib import Path
# import miDb
# import graphql
# import api

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)

dependencias = {
    "db": "db", # miDb,
    "api": "api", # api,
    "graphql": "graphql" # graphql
}

# Load se encargara de tomas cada uno de los paths(paquetes) e importarlos, ademas ejecutar sus init
def load(p):
    #print(str(p))
    paquete = __import__(str(p).replace("/", ".")) #__import__ es para importar paquetes de manera dinamica
    #paquete.init() por si algunos paquetes no tienen el metodo init, controlar el fallo
    try:
        paquete.init(**dependencias)
    except:
        print("El paquete no tiene init")

list(map(load, paths))
