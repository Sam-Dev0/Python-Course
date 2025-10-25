#mi_archivo =open('01_prueba.txt','r') # modo solo lectura
#mi_archivo.write('soy otra linea') # presenta error, el archivo es modo solo  lectua

"""
mi_archivo =open('01_prueba.txt','a') # agrega una linea al final \n es para crear el salto de lina
mi_archivo.write('\nsoy otra linea') 

mi_archivo.writelines(['\n','Hola ','como ','estas ','una linea mas larga'])

mi_archivo_2 =open('02_prueba.txt','w') # reescribe el archivo utilizado, si no existe crea uno nuevo
mi_archivo_2.write('Este es un texto')
mi_archivo_2.write('\nEste es otro texto')
"""

registro_ultima_sesion =['Federico','20/12/2021','08:17;32 hs','Sin errores de carga']

ejercicio = open('registro.txt','a')

for x in registro_ultima_sesion:
    ejercicio.writelines(x+'\t')
ejercicio.close() 

ejercicio=open('registro.txt','r')
print (ejercicio.read())
ejercicio.close()