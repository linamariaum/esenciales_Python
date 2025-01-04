lista_vacia = list()

mascotas = ["Pulga", "Rayas", "Pulga", "Chanchito"]

mascotas.insert(1, "Melvin")
mascotas.append("Peque")
mascotas.remove("Pulga")
mascotas.pop()
mascotas.pop(1)
del mascotas[0]
mascotas.clear()

print(mascotas)

numeros = [2, 4, 1, 45, 75, 22]
numeros.sort()
numeros.sort(reverse=True)

numeros2 = sorted(numeros) #Devuelve una nueva lista
numeros2 = sorted(numeros, reverse=True)

print(numeros)
print(numeros2)

usuarios = [[2, "Chanchito"], [1, "Rayas"], [5, "Pulga"]]
usuarios2 = [["Chanchito", 2], ["Rayas", 1], ["Pulga", 5]]
usuarios.sort()


def ordena(elemento):
    return elemento[1]

usuarios2.sort(key=ordena)
usuarios2.sort(key=ordena, reverse=True)
# o
usuarios2.sort(key=lambda elemento:elemento[1]) # lambda parametro:valorRetorno

# compresion listas
nombres = []
for usuario in usuarios2:
    nombres.append(usuario[0])
print(nombres)
# o, con transformación
nombres = [usuario[0] for usuario in usuarios2] # expresion for item in items ## Esto basicamente es un MAP
# o con filtrado ## Esto basicamente es un FILTER
usuariosCondicion = [usuario for usuario in usuarios2 if usuario[1] > 2]
# o filtrar y transformar al mismo tiempo
nombresUsuariosCondicion = [usuario[0] for usuario in usuarios2 if usuario[1] > 2]

nombre2 = list(map(lambda usuario: usuario[0], usuarios2))
usuariosCondicion2 = list(filter(lambda usuario: usuario[1] > 2, usuarios2))
