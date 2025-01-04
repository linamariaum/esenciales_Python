# Es una coleccion de datos agrupados por llave y valor

punto = { "x": 25, "y": 50}
print(punto["x"])
punto["z"] = 45

print(punto["lala"]) # Error en compilacion KeyError, llave no exite en el diccionario
if "lala" in punto:
    print(punto["lala"])

print(punto.get("y"))
print(punto.get("lala")) # No saca error, devuelve NONE ya que esa llave no existe
print(punto.get("lala", 97)) # Esta sintaxis indica que si la llave "lala" no existe en el diccionario entonces por defecto arroje el valor de 97

del punto["x"]
print(punto)
punto["x"] = 25

for valor in punto: # valor es la llave
    print(valor)
    print(punto[valor])
    print(valor, punto[valor])

for valor in punto.items(): # valor es una tupla llave-valor
    print(valor)

for llave, valor in punto.items(): # usando desempaquetado de los iterables, se puede sacar el valor y la llave en varibales
    print(llave, valor)

usuarios = [
    {
        "id": 1,
        "nombre": "Chanchito"
    },
    {
        "id": 2,
        "nombre": "Feliz"
    },
    {
        "id": 3,
        "nombre": "Nicolas"
    },
    {
        "id": 4,
        "nombre": "Felipe"
    },
]

for usuario in usuarios:
    print(usuario["nombre"])
