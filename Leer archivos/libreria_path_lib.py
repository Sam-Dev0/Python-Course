from pathlib import Path,PureWindowsPath
"""
carpeta = Path('C:/Users/CET56/Documents/python/Alternativa/nueva_pruba.txt')
print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)

if not carpeta.exists():
    print('La carpeta no existe')
else:
    print('la carpeta existe')

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)
"""
"""
#crear archivos, mover archivos, enumerar archivos, crear rutas

base = Path.home() #directorio raiz del usuario actual
print(f'la ruta raiz es: {base}')

guia = Path ('Bogota','Chapinero')
print(guia)

guia = Path(base,'Bogota','Capinero')
print(guia)

guia_2 = Path(base,'America','Suramerica','Colombia','Cundinamarca','Bogota','mi_archivo.txt')
print(guia_2)
guia_3 = guia_2.with_name('la Candelaria.txt')
print(guia_3)
print(guia_3.parent.parent)

"""
## archivos dentro de la carpeta europa
"""
guia4 = Path('C:/Users/CET56/Europa')

for x in Path(guia4).glob('*.txt'):
    print(x)
"""
## archivos dentro de la carpeta europa y sus subcarpetas
"""
guia4 = Path('C:/Users/CET56/Europa')
n=0
for x in Path(guia4).glob('**/*.txt'):
    print(x)
    n=n+1
print('La cantidad de archivo es',n)
"""

ruta = Path('C:/Users/CET56/Downloads')
n=0

for x in Path(ruta).glob('**/*.docx'):
    n=n+1
print('La cantidad de archivo es',n)
