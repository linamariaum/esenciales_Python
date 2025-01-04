nombre = "Nicolas"
apellido = "Vasquez"
nombre_completo = f"{nombre} {apellido} {2*9} {2*3}"
print(nombre_completo)

animal = "gatico lupita vaco"
texto = "    espacios adelante y atras     "
print(animal.upper())
print(animal.capitalize())
print(animal.title())
print(texto.strip())
print(texto.rstrip())
print(texto.lstrip())
print(texto.strip().capitalize())

print(animal.find("Iris"))
print(animal.find("vaco"))
print(animal.find("Lupita"))
print(animal.find("lupita"))
print(animal.replace("lu", "Lu"))
print("lupita" in animal)
print("Lupita" in animal)
print("Lupita" not in animal)
