# xargs, x numero de argumentos, requiere explicitamente el * para indicar que es un argumento iterable

def sumaF(a, b):
    print (a+b)

sumaF(2, 5)
#sumaF(3, 4, 5, 6, 7) # Falla y habria que estar creando metodos para las distintas cantidades de argumentos

def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(2, 5)
suma(2, 5, 4)
suma(3, 4, 5, 6, 7)


#---------------------------------------------------
# kwargs, keyWord arguments, requiere explicitamente el **

def get_product(**datos):
    print(datos)
    print(datos["id"], datos["name"])

#get_product("id") # Falla porque si o si al ser un kwargs, se le debe indicar el nombre al argumento, diccionario
get_product(id="id")
get_product(id="23", name="Telefono", desc="Producto telefono")
