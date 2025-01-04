from pprint import pprint
# 1. Eliminar los espacios en blanco de un string y devolver una lista con los caractres restantes
# 2. Contar en un diccionario cuantas veces se repiten los caracteres de un string
# 3. Ordenar las llaves de un diccionario por el valor que tienen y devolver una lista que contiene tuplas. [("a", 3), ("b", 2), ("c", 4)]
# 4. De un listado de tuplas, devolver las tuplas que tengan el mayor valor.
# 5. Crear un mensaje que diga: Los caracteres que mas se repiten con 4 repeticiones son [lista]
# 6. Juntar la solucion de los ejercicios anteriores para encontrar los caracteres que mas se repiten de un string

# 1
texto = "    Arcoiris de           primavera que aparece despues de la tormenta    "
texto = texto.strip().lower().replace(" ", "")
print(texto)
lista = []
for letra in texto:
    lista.append(letra)
print(lista)
lista2 = list(texto)
print(lista2)

#otra solucion
string = "Hola mundo este es mi string"
def quita_espacios(texto):
    return [letra for letra in texto if letra != " "]
sin_espacios = quita_espacios(string.lower())
print(sin_espacios, "\n")

# 2
diccionario = {}
print(diccionario)
for letra in texto:
    if letra in diccionario:
        diccionario[letra] += 1
    else:
        diccionario[letra] = 1
pprint(diccionario, width=1)
print(diccionario, "\n")

# 3
diccionario_ordenado = {}
# for llave, valor in diccionario.items():
#     print(llave, valor)
#     for llave2, valor2 in diccionario.items():
#         if valor >= valor2:
lista_tupla_ordenado_asc = sorted(
    diccionario.items(),
    key=lambda key: key[1]
)
lista_tupla_ordenado_desc = sorted(
    diccionario.items(),
    key=lambda key: key[1],
    reverse=True
)
print(lista_tupla_ordenado_desc)
lista_tuplas = []
for tupla in diccionario.items():
    lista_tuplas.append(tupla)
print(lista_tuplas, "\n")

# 4
def mayores_tuplas(lista):
    valor_maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if valor_maximo > orden[1]:
            print("entro al if")
            break
        respuesta[orden[0]] = orden[1]
    return respuesta

diccionario_solo_mayores = mayores_tuplas(lista_tupla_ordenado_desc)
print(diccionario)
print(diccionario_solo_mayores)
lista_tuplas_mayores = []
for tupla in diccionario_solo_mayores.items():
    lista_tuplas_mayores.append(tupla)
print(lista_tuplas_mayores, "\n")

# 5
def crea_mensaje(diccionario_entrada):
    mensaje = "Los caracteres que mas se repiten son: \n"
    for llave, valor in diccionario_entrada.items():
        mensaje += f"- {llave} con {valor} repeticiones"
    return mensaje
mensaje = crea_mensaje(diccionario_solo_mayores)
print(mensaje)