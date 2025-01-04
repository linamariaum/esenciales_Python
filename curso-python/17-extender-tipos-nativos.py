lista1 = list([1, 2, 3])
lista1.append(4) # Para agregar un valor al final de la lista
#No existe un metodo directo para agregar al inicio
lista1.insert(0, 0) # Para agregar un valor al inicio de la lista
print(lista1)
# Se puede hacer algo más intuitivo para nuestra logica extendiendo los tipos nativos,asi

class Lista(list):
    def agregar_al_inicio(self, item): # tambien se podría llamar a este metodo prepend
        self.insert(0, item)

lista = Lista([1, 2, 3])
lista.agregar_al_inicio(0)
lista.append(4)
print(lista)
