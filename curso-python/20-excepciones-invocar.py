# def divisionF(n=0):
#     return 5 / n

# divisionF()

# -------------------------------
def division(n=0):
    if n == 0:
        #raise Exception("Lanzar una excepcion muy general")
        raise ZeroDivisionError("No se puede dividir por cero", f"{n}")
    return 5 / n

try:
    division()
except ZeroDivisionError as e:
    print(e)


# Aqui al final, podemos encontrar la gerarquia de las excepciones
# https://docs.python.org/3/library/exceptions.html