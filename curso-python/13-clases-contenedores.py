class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"

class Categoria:
    productos = []

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)

balon = Producto("Balon", 83000)
bicicleta = Producto("Bicicleta", 250000)
patin = Producto("patin", 135000)
deportes = Categoria("Deportes", [balon, bicicleta])
deportes.agregar(patin)
deportes.imprimir()