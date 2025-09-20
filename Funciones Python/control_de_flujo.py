#Verificar la contraseña correcta
n = int(input("Ingrese la contraseña: "))
print("Contraseña correcta")
while n != 1234:
  print("Contraseña incorrecta")
  n = int(input("Ingrese un la contraseña: "))


#Calcular descuento de compra
compra = float(input("Ingrese el valor de la compra:"))
p = 0.25
r = 0
o = 0
if compra >= 1000:
  r = compra * p
  o = compra - r
  print("El descuento es de", r, "Y le queda en", o)
else:
  print("No aplica")


#Mostrar mensaje segun calificacion
note = int(input("Ingrese la nota: "))
nota = 0
match note:
    case 1 if nota >=0 and nota <=2:
      print("Pesimo")
    case 2 if nota >=3 and nota == 6:
      print("Regular")
    case 3 if nota >= 7 and nota == 10:
      print("Excelente")


for x in range(1, 11):
  print(x)


n = 100
suma = 0
while n > 0:
  digito = n + n
  suma += digito
  n //= n
print("La suma de los digitos es:", suma)


tabla = int(input("Que tabla se necesita: "))
i = 1
r = 0
while i <= 10:
  r = tabla * i
  print(tabla, "x", i, "=", r)
  i += 1


#Leer numeros hasta que el usuario ponga 0
n = int(input("Ingrese un numero: "))
while n != 0:
  n = int(input("Ingrese un numero: "))


#Calcular la suma de los digitos de un numero
n = int(input("Ingrese un numero: "))
suma = 0
while n > 0:
  digito = n % 10
  suma += digito
  n //= 10
print("La suma de los digitos es:", suma)


#Multiplicacion con for
r = 0
for tabla in range(1, 11):
  print("Tabla del ", tabla)
  for cont in range(1, 11):
    r = tabla * cont
    print(tabla, "x", cont, "=", r)