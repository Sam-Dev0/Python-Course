import os

ruta =os.getcwd()
print(ruta)

otra_ruta =os.chdir('C:\\Users\\CET56\\Documents\\python\\Alternativa')
archivo = open('nueva_pruba.txt')
print(archivo.read())
archivo.close()

# crear carpetas

#ruta =os.makedirs('C:\\Users\\CET56\\Documents\\python\\Alternativa\\otra')
ruta_archivo = 'C:\\Users\\CET56\\Documents\\python\\Alternativa\\nueva_pruba.txt'
elemento=os.path.basename(ruta_archivo)
print(elemento)

elemento_y_ruta=os.path.split(ruta_archivo)
print(elemento_y_ruta)

#os.rmdir('C:\\Users\\CET56\\Documents\\python\\Alternativa\\otra')

archivo = open('C:\\Users\\CET56\\Documents\\python\\Alternativa\\nueva_pruba.txt')

from pathlib import Path
carpeta = Path('C:/Users/CET56/Documents/python/Alternativa')
archivo = carpeta /'nueva_pruba.txt'
mi_archivo = open(archivo)
print(mi_archivo.read())

mi_archivo.close()
