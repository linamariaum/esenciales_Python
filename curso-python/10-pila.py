# Las pilas son LIFO, ultimo que llega primero que sale

pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)
elemento = pila.pop()
print(elemento)
print(pila)
print(pila[-1])

if not pila:
    print("Pila vacia")
