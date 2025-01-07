class MiError(Exception):
    "Esta clase es para representar mi error"

    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self):
        return f"Codigo: {self.codigo} - {self.mensaje}"

def division(n=0):
    if n == 0:
        #raise Exception("Lanzar una excepcion muy general")
        raise MiError("No se puede dividir por cero", f"{n}")
    return 5 / n

try:
    division()
except MiError as e:
    print(e)
