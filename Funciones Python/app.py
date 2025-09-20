"""Ejercicio 1- hacer 3 funciones de cambio de moneda de pesos a x"""

"""OPCION 1(Cada una por separado)"""
#cambio a dolar
def dolar(operacion):
   operacion = valor * 0.00026
   return operacion
valor = float(input("Digite el valor que desea convertir a dolar: "))
print(dolar(valor))

#cambio a euro
def euro(operacion):
   operacion = valor * 0.00022
   return operacion
valor = float(input("Digite el valor que desea convertir a euro: "))
print(euro(valor))

def yen(operacion):
   operacion = valor * 0.038
   return operacion
valor = float(input("Digite el valor que desea convertir a yenes: "))
print(yen(valor))

#------------------------------------------------------------------------------------------------------#

"""Ejercicio 2- hacer 1 funcion para cambio de moneda preguntando que moneda se requiere y su valor"""

"""OPCION 2 (llamando a la que el usuario requiera)"""
#Define cada funcion
def dolar(operacion):
   operacion = operacion * 0.00026
   return operacion

def euro(operacion):
   operacion = operacion * 0.00022
   return operacion

def yen(operacion):
   operacion = operacion * 0.038
   return operacion
#Le muestra las opciones y le pregunta al usuario
print("Seleccione la moneda que desea realizar: ")
print(1 ,"convertir a dolares")
print(2 ,"convertir a euros")
print(3 ,"convertir a yenes")
opcion = int(input("Ingrese el numero de opcion: "))

#Pregunta el valor que desea convertir
valor = float(input("Ingrese el valor que desea convertir :"))

#Logica dependiendo de la eleccion del usuario
if opcion == 1:
   resultado = dolar(valor)
   print("El valor del dolar es:", resultado)
elif opcion == 2:
   resultado = euro(valor)
   print("El valor del euro es:", resultado)
elif opcion == 3:
   resultado = yen(valor)
   print("El valor del yen es de:", resultado)
else:
   print("Opcion no valida")