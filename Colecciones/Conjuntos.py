# 1. Crear un conjunto con los elementos de una lista
lista = [1, 2, 2, 3, 4, 4, 5]
conjunto = set(lista)
print("\n1. Conjunto creado:", conjunto)

# 2. Agregar nuevo elemento
conjunto.add(6)
print("2. Conjunto con nuevo elemento:", conjunto)

# 3. Eliminar elemento
conjunto.discard(2)
print("3. Conjunto sin el número 2:", conjunto)

# 4. Comprobar si un elemento está
print("4. ¿Está el número 3?", 3 in conjunto)

# 5. Unión de dos conjuntos
A = {1, 2, 3}
B = {3, 4, 5}
print("5. Unión:", A | B)

# 6. Intersección
print("6. Intersección:", A & B)

# 7. Diferencia
print("7. Diferencia A - B:", A - B)

# 8. Vaciar conjunto
conjunto.clear()
print("8. Conjunto vacío:", conjunto)

# 9. Crear conjunto a partir de cadena
cadena = "python"
set_cadena = set(cadena)
print("9. Conjunto de caracteres:", set_cadena)

# 10. Recorrer conjunto
print("10. Elementos del conjunto:")
for elemento in set_cadena:
    print("-", elemento)
