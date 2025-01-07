# Los ambientes virtuales es para manejar y compartir de una manera más eficiente las dependencias de nuestro proyecto

# Comando
# > python -m venv env 
# Y en el IDE/Editor se debe seleccionar el interprete de python
# Luego hay que activar el ambiente virtual que se ha creado, para Windows:
# > env\bin\activate.bat
# Al activarlo el ide/editor en la consola nos mostrará que estamos en el entorno virtual todo el tiempo hasta desactivarlo
# Procedemos a instalar los paquetes que necesitemos y estos quedaran en el ambiente virtual

# Para desactivar el ambiente virtual
# > deactivate


# -------------------------------------------------------------------------------

# Otra forma es usando pipenv para los ambientes virtuales, para esto
# > pip install pipenv
# Ya podemos empezar a instalar nuestros paquetes
# > pipenv install "paquete"
# esto creara en nuestro proyecto los archivos de "Pipfile" y "Pipfile.lock"
# pipenv no crea una carpeta del entorno virtual dentro de la carpeta de nuestro proyecto, pero si la crea en otra ubicación
# para revisar la ubicacion en la que quedó el ambiente virtual:
# > pipenv --venv
# mostrara en consola la ruta, ejm c:/users/virtualenvs/mienv
# Luego hay que activar el ambiente virtual que se ha creado, mas bien seleccionar el interprete de pipenv en el ide/editor
# En VS veremos en la parte inferior derecha, la version de python y el interprete que se este usando
# Para usar el ambiente virtual que creamos dentro de la terminal (Esto es como activarlo):
# > pipenv shell
#Al activarlo el ide/editor en la consola nos mostrará que estamos en el entorno virtual todo el tiempo hasta desactivarlo/salir
# Para listar los paquetes y sus dependencias que tenemos instalados:
# > pipenv graph
# Si quisieramos desinstalar algun paquete de nuestro entorno virtual:
# > pipenv uninstall "paquete"
# Este comando desinstalara el paquete indicado (pero no sus dependencias) y además nos actualizará nuestros archivos Pipfile y Pipfile.lock
## pipenv no desinstaló las dependencias del paquete recien eliminado, porque no sabe si otro paquete que estemos usando las utiliza, así que las deja ahí. Pero no estan incluidas
## en nuestros archivos Pipfile por lo que para una proxima instalacion NO se bajaran esas dependencias ya que no son usadas en ninguno de nuestros paquetes.
# Para salir del ambiente virtual:
# > exit
# si quisieramos eliminar por completo el ambiente virtual:
# > rm -rf "ubicacion del entorno virtual"
# ejm: rm -rf c:/users/virtualenvs/mienv
# Cuidado! si solo ejecutamos "rm -rf" sin especificarle ruta, borrará todos los entornos virtuales que existan


# Para desinstalar paquetes que no esten en el entorno virtual sino a nivel global:
# > pip uninstall "paquete"
