# Collection de elementos ordenadas pero que no se pueden modificar
# Ni agregar ni borrar ningun valor

tuple_colores = ("Rojo", "Verde", "Amarillo")

print(tuple_colores)

# Largo de las tuplas
print("Length", len(tuple_colores))

# Acceder a cada elemento
for color in tuple_colores:
    print(color)
    

# Cuenta cuantas veces hay un elemento
print(tuple_colores.count("Rojo"))