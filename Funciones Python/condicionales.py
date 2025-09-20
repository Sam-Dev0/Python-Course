#Guardar un nombre
n = "samuel"
print("Yo soy",n)

#Sumar dos numeros
a = 10
b = 5
c = a + b
print("El resultado es",c)

#Guardar la edad
edad = 18
print("Tengo",edad,"años")

#Variable que indica si soy estudiante
es_Estudiante = True
print("Samuel es estudiante?", es_Estudiante)

#Guarda el precio y calcula el iva
precio = 100
iva = precio * 0.19
precio_fin = precio + iva
print("El iva es", precio_fin)

#Calcular el area de un rectangulo
base = 10
altura = 5
area = base * altura
print("El area del rectangulo es", area)

#Hallar el perimetro de un circulo
radio = 5
pi = 3.14159
perimetro = 2 * pi * radio
print("El perimetro del circulo es", perimetro)

#Convertir grados celcius a fahrenheit
celsius = 31
fahrenheit = (celsius * 9/5) + 32
print("31 grados celsius son", fahrenheit, "grados fahrenheit")

#Calcular el promedio de 3 notas
nota1 = 5.0
nota2= 3.5
nota3 = 2.8
promedio = (nota1 + nota2 + nota3) / 3
print("El promedio de las notas es", promedio)

#Residuo de dividir entre 5
n = 25
r = n / 5
print("El residuo es", r)

#Si un numero es mayor que otro
n1 = 10
n2 = 5
if n1 > n2:
  print("El numero", n1,"es mayor")
else:
  print("el numero", n2,"es mayor")

#Comprobar si dos numeros son iguales
n1 = 44
n2 = 128
if n1 == n2:
  print("Los numeros son iguales")
else:
  print("Los numeros no son iguales")


#Evaluar si un numero es positivo y par
n = 4
if n > 0 and n % 2 == 0:
  print("El numero es par")
else:
  print("El numero es impar")


#Verificar si un estudiante aprueba nota(>=3.0)
nota = 2.8
if nota >= 3.0:
  print("El estudiante aprueba")
else:
    print("El estudiante no aprueba")


#Determinar si es mayor de edad y estudiante
edad = 18
es_Estudiante = True
if edad >= 18 or es_Estudiante:
  print("Es mayor de edad y no estudiante")


#Calificaciones (>=4.5"Excelente" -- >=3.0 "Bueno" -- < 3.0 "Reprobo")
nota = float(input("ingrese la nota: "))
if nota < 0 or nota > 5:
  print("Nota invalida")
elif nota >= 4.5:
  print("Excelente")
elif nota >= 3.0:
  print("Bueno")
else:
  print("Reprobo")
  
