# La diferencia entre modulos y paquetes es:
# - Modulos apuntan a archivos
# - Paquetes apuntan a carpetas

## Creamos el paquete (carpeta) usuarios
## Para transformar todo el contenido de la carpeta usuarios, en un paquete que pueda ser usado, debemos crear el archivo __init__ (solo crearlo, esta vacío)
## Al la carpeta contener el archivo __init__ con esto Python ya sabe que toda la carpeta es un paquete

### Sub-paquetes
### Es cuando por organizacion del codigo decidimos tener más niveles de encarpetado
### Ejm, crearemos la carpeta acciones dentro de la actual carpeta usuarios. Con su archivo __init__
### y pasaremos para esta ubicacion el archivo de acciones (Crearemos una copia llamada dos como sufijo)

#### Referenciando Sub-paquetes
#### invocar metodos hacia arriba o hacia arriba de la gerarquia
#### Ejm main.py