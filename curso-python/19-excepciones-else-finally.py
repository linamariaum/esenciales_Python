try:
    n1 = int(input("Ingrese primer numero: "))
except Exception as e:
    print("Ocurrió un error")
else: # Se ejecuta siempre y cuando no haya habido alguna excepcion
    print("No ocurrió ningún error")


try:
    n1 = int(input("Ingrese primer numero: "))
except Exception as e:
    print("Ocurrió un error")
finally: # Se ejecuta siempre (Cuando hay y cuando no hay excepcion)
    print("Se ejecuta siempre")


# La instrucción else y la finally se pueden encadenar
try:
    n1 = int(input("Ingrese primer numero: "))
except Exception as e:
    print("Ocurrió un error")
else:
    print("No ocurrió ningún error")
finally:
    print("Se ejecuta siempre")
