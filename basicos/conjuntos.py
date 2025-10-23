# Es una collecion de elemnetos desordenado, no se puede acceder por un índice

colores = {"Verde", "Azul", "Amarillo", "Rojo"}

print(colores)

print("Length", len(colores))

# Acceder a cada uno
for color in colores:
    print(color)
    
# Acceder a una posicion concreta no se puede, porque no tiene índices
# does not support indexing

# Podes agregar o quitar con add y remove
colores.add("Naranja")
colores.add("Negro")

print(colores)

colores.remove("Verde")
print(colores)

# Borra todos
colores.clear()
print(colores)