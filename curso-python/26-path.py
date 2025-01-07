# Rutas
from pathlib import Path

# # Crear una ruta en Windows
# Path(r"C:\Archivos de Programa\CarpetaNueva") # Ruta absoluta
# # Crear una ruta en Linux/Mac
# Path("/usr/bin") # Ruta absoluta

# #
# Path()
# Path.home()
# # En la carpeta en la que me encuentro, crea este path, ruta relativa
# Path("one/__init__.py")

path = Path("26-hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

p = path.with_name("chancito.exe")
print(p)
p = path.with_suffix(".bat")
print(p)
