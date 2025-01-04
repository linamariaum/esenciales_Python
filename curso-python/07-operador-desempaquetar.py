lista1 = [1, 2, 3, 4]
tupla = (1, 2, 3, 4)
print(*lista1)
print(*tupla)

lista2 = [5, 6, 7]
combinada = [*lista1, *lista2]
combinada2 = ["Hola", *lista1, "mundo", *lista2]

punto1 = {"x": 19}
punto2 = {"y": 15}
nuevoPunto = {**punto1, **punto2}
print(nuevoPunto)
punto11 = {"x": 19, "y": "hola"}
nuevoPunto2 = {**punto11, **punto2} # asigna al nuevo diccionario los valores de derecha a izq, y al encontrarse una llave que ya existe la omite y continua
print(nuevoPunto2)
nuevoPunto3 = {**punto1, "lala": "arcoiris", **punto2, "z": "mundo"}
print(nuevoPunto3)
