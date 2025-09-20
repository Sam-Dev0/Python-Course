#Planteamiento: Crear una función que reciba dos números y devuelva su suma.
def suma (a, b):
    return a + b

print(suma(5, 3))

#Planteamiento: Crear una función que convierta grados Celsius a Fahrenheit.
def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

print(celsius_a_fahrenheit(30))

#Planteamiento: Crear una función que calcule el promedio de una lista.
def promedio(lista):
    suma = 0
    for num in list:
        suma = suma + num
    return suma / len(lista)

print(promedio([2, 4, 6, 8]))


#Planteamiento: Crear una función que determine si un número es par.
def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False
    print(es_par(10))

es_par();


#Planteamiento: Crear una función que calcule el área de un rectángulo.Código con errores:def area_rectangulo(base, altura)return base * altoprint(area_rectangulo(5, 3))6. Contar palabras en una frasePlanteamiento: Crear una función que cuente cuántas palabras tiene una frase.Código con errores:def contar_palabras(frase):palabras = frase.splitreturn len(palabra)print(contar_palabras("Hola mundo con Python"))
def area_rectangulo(base, altura):
    return base * altura

print(area_rectangulo(5, 3))


#Planteamiento: Crear una función que cuente cuántas palabras tiene una frase.
def contar_palabras(frase):
    palabras = frase.split
    return len(frase)

print(contar_palabras("Hola mundo con Python"))


#Planteamiento: Crear una función que reciba tres números y retorne el mayor.
def mayor(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c 
    print(mayor(4, 9, 2))


#Planteamiento: Una contraseña es válida si tiene 8 o más caracteres.
def validar_contrasena(contra):
    if len(contra) >= 8:
        return True
    else:
        return False
    print(validar_contraseña("python123"))


#Planteamiento: Crear una función que calcule el factorial de un número entero.
def factorial(n):
    resultado = 1
    for i in range(1, n):
        resultado *= i
    return resultado
print(factorial(5))    


#Planteamiento: Crear una función que muestre la tabla de multiplicar de un número.
def tabla(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
tabla(7);

