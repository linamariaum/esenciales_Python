# Al crear los ambientes virtuales mediante pipenv
# Se crean en nuestro proyecto los archivos de "Pipfile" y "Pipfile.lock"
# En estos se especifica las dependencias y las versiones de esas dependencias usadas en nuestro proyecto (similar al pom o gradle en java)

# Con los entornos virtuales se facilita el manejo y la forma de compartir las dependencias de nuestro proyecto.
# Suponiendo que no tenemos el entorno virtual creado, pero si tenemos el proyecto con sus respectivos "Pipfile" y "Pipfile.lock", entonces:
# > pipenv install
# Este comando creará el entorno virtual y al mismo tiempo instalara las dependencias especificadas en el archivos Pipfile
# Pero si no quisieramos que instale lo del Pipfile sino que instale lo del Pipfile.lock (que aquí se encuentra todo mucho mas detallado), entonces:
# > pipenv install --ignore-pipfile
# Este comando creará el entorno virtual y al mismo tiempo instalara las dependencias especificadas en el archivo Pipfile.lock


# Para que pipenv nos revise las versiones que tenemos instaladas versus las versiones nuevas de los paquetes:
# > pipenv update --outdated
# Este comando nos listara las versiones que tenemos instaladas vs su version más reciente, siempre y cuando al instalar por primera vez
# determinado paquete no le hayamos especificado de forma directa la verison que deseamos que nos instale. De ser así, al verificar el vs de las versiones,
# nos mostrara en consola que se determinado paquete nosotros le seteamos una version particular en especifico

# Para que nos actualice un paquete en especifico a su version mas actual:
# > pipenv update "paquete"
# Para que nos actualice todos los paquetes a su version mas actual:
# > pipenv update
# Esto actualizará nuestros archivos Pipfile




# -------------------------
# archivo .env
# NOMBRE_CONSTANTE = "token"

# import os
# apiKey = os.environ.get("NOMBRE_CONSTANTE")
# print(apiKey)

# excel openpyxl
