try:
    n1 = int(input("Ingrese primer numero: "))
except:
    print("Ocurrio un error")

# Para manejar todos los errores
try:
    n1 = int(input("Ingrese primer numero: "))
except Exception as e:
    print("Ocurrio un error")
    print(type(e))

# Para manejar un error en especifico
try:
    n1 = int(input("Ingrese primer numero: "))
except ValueError as e:
    print("El valor ingresado no es valido, ingrese un valor que corresponda")

# Para manejar errores en especifico
try:
    n1 = int(input("Ingrese primer numero: "))
    variablex
except ValueError as e:
    print("El valor ingresado no es valido, ingrese un valor que corresponda")
except NameError as e:
    print("Ocurrio un error!")
