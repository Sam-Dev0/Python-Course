# 1. Crear un diccionario con tres pares clave-valor
persona = {"nombre": "Samuel", "edad": 18, "profesion": "Estudiante"}
print("\n1. Diccionario:", persona)

# 2. Acceder a un valor por su clave
print("2. Nombre:", persona["nombre"])

# 3. Modificar valor existente
persona["edad"] = 19
print("3. Edad modificada:", persona)

# 4. Añadir nueva clave-valor
persona["pais"] = "Colombia"
print("4. Diccionario con nueva clave:", persona)

# 5. Eliminar una clave
persona.pop("profesion")
print("5. Diccionario sin 'profesion':", persona)

# 6. Obtener claves y valores
print("6. Claves:", persona.keys())
print("   Valores:", persona.values())

# 7. Recorrer diccionario
print("7. Claves y valores:")
for clave, valor in persona.items():
    print(f"- {clave}: {valor}")

# 8. Comprobar si una clave existe
print("8. ¿Existe 'edad'?", "edad" in persona)

# 9. Copiar el diccionario
copia = persona.copy()
print("9. Copia del diccionario:", copia)

# 10. Vaciar el diccionario
persona.clear()
print("10. Diccionario vacío:", persona)