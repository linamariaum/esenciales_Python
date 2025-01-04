# un set significa conjunto o grupo

primer = {1, 1, 2, 2, 3, 4} # Al ser un set remueve el dato repetido para quedar solo con una ocurencia por valor
primer.add(5)
primer.remove(1)

listaSegundo = [3, 4, 5, 6, 6, 7]
segundo = set(listaSegundo)

print(primer | segundo) # hace una union
print(primer & segundo) # hace una interseccion, saca los que estan en comun
print(primer - segundo) # hace una diferencia, saca lo que unicamente esta en el primero, es decir, al primero le quita lo que tenga en comun con el segundo
print(primer ^ segundo) # hace una diferencia simetrica, saca los que unicamente estan en el primero y unicamente estan en el segundo

# No se puede acceder a los elementos de un set
#segundo[0] #Error
