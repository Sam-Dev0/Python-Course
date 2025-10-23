# 1. Crear una tupla con 5 colores
colores = ("rojo", "verde", "azul", "amarillo", "negro")
print("\n1. Tupla de colores:", colores)

# 2. Convertir lista en tupla
tupla_numeros = tuple(numeros)
print("2. Lista convertida en tupla:", tupla_numeros)

# 3. Contar ocurrencias de un elemento
print("3. El número 5 aparece:", tupla_numeros.count(5), "veces")

# 4. Obtener la longitud
print("4. Longitud de la tupla:", len(tupla_numeros))

# 5. Acceder al tercer elemento
print("5. Tercer elemento:", colores[2])

# 6. Mostrar elementos uno por uno
print("6. Elementos de la tupla:")
for color in colores:
    print("-", color)

# 7. Unir dos tuplas
tupla2 = (10, 20, 30)
tupla_unida = tupla_numeros + tupla2
print("7. Tuplas unidas:", tupla_unida)

# 8. Porción de la tupla (segundo al cuarto)
print("8. Slice (2° al 4°):", tupla_unida[1:4])

# 9. Valor máximo y mínimo
tupla_numerica = (4, 7, 1, 9, 3)
print("9. Máximo:", max(tupla_numerica), "Mínimo:", min(tupla_numerica))

# 10. Comprobar si un elemento está en la tupla
print("10. ¿Está el número 7?", 7 in tupla_numerica)
