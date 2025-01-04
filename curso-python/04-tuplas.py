# Tuplas son inmutables, es decir despues de creada no se puede agregar elementos, ni quitar, ni modificar

numeros = (1, 2, 3) + (4, 5, 6)

lista = [1, 2]
punto = tuple(lista)
menosNumeros = numeros[:2]
listaNumeros = list(numeros)
