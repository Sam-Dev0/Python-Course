# 1. Crear una lista con los números del 1 al 10 y mostrarla
numeros = list(range(1, 11))
print("1. Lista del 1 al 10:", numeros)

# 2. Solicitar 5 números al usuario y mostrar la suma
numeros_usuario = []
for i in range(5):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros_usuario.append(num)
print("2. Suma de los números:", sum(numeros_usuario))

# 3. Mostrar los elementos de la lista en orden inverso
print("3. Lista invertida:", numeros_usuario[::-1])

# 4. Comprobar si un elemento dado por el usuario está en la lista
buscar = int(input("Ingrese un número para verificar si está en la lista: "))
if buscar in numeros_usuario:
    print(f"4. El número {buscar} está en la lista.")
else:
    print(f"4. El número {buscar} no está en la lista.")

# 5. Eliminar el último elemento de la lista
numeros_usuario.pop()
print("5. Lista sin el último elemento:", numeros_usuario)

# 6. Contar cuántas veces aparece el número 2
print("6. El número 2 aparece:", numeros_usuario.count(2), "veces")

# 7. Crear una lista con las palabras de una frase
frase = input("Ingrese una frase: ")
palabras = frase.split()
print("7. Lista de palabras:", palabras)

# 8. Concatenar dos listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
concatenada = lista1 + lista2
print("8. Listas concatenadas:", concatenada)

# 9. Obtener elementos únicos (sin repeticiones)
lista_repetida = [1, 2, 2, 3, 3, 4]
unicos = list(set(lista_repetida))
print("9. Elementos únicos:", unicos)

# 10. Multiplicar todos los elementos de la lista por 2
doble = [n * 2 for n in numeros]
print("10. Elementos multiplicados por 2:", doble)