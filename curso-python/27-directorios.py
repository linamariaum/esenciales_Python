from pathlib import Path

path = Path("curso-python")
# path.exists()
# path.mkdir() # Crear directorio
# path.rmdir() # Remover directorio, solo si su contenido esta vacio
# path.rename("27-chanchito-feliz")

print(path.iterdir)

for p in path.iterdir():
    print(p)

archivos = [p for p in path.iterdir() if not p.is_dir()]
archivos_py = [p for p in path.glob("*.py")]
archivos_01 = [p for p in path.glob("01-*.py")]
archivos_py_niveles = [p for p in path.glob("**/*.py")]
archivos_py_niveles_otraForma = [p for p in path.rglob("*.py")] # Recursivo
carpetas = [p for p in path.iterdir() if p.is_dir()]
print(carpetas)
