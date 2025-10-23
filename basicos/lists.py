# Lista
# Conjunto de elementos que esta ordeanda y que se pueden

colores = ["Rojo", "Amarillo", "Verde", "Azul"]

print(colores)

# Modificar un elemento
colores[0] = "Naranja"

print(colores)

# El numero de elementos de la lista
q_elements = len(colores)

print("Length", q_elements)

# Agregar un elemento al final
colores.append("Gris")

print(colores)

# Quitar un elemento
colores.remove("Amarillo")

print(colores)

# Recorrer la lista con un bucle for
for color in colores:
    print(color)
    
# Borra todos los elementos
colores.clear()

print(colores)