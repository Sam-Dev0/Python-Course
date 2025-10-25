mi_archivo=open('01_Prueba.txt')
print(mi_archivo)
print(mi_archivo.read()) #lee todo el archivo#
una_linea=mi_archivo.readline()#metodo para leer una linea
print(una_linea)
"""el codigo no muestra todas las lineas porque ya se ejecuto la lectura de todo el archivo
el puntero esta en la ultima linea, al utilzar readline ya no hay nada que leer"""

mi_archivo.seek(0)
una_linea=mi_archivo.readline()
print(una_linea)

otra_linea=mi_archivo.readline()
print(otra_linea)

otra_linea_2=mi_archivo.readline()
print(otra_linea_2)


todas_lineas =mi_archivo.readlines()
print(todas_lineas)




mi_archivo.close()