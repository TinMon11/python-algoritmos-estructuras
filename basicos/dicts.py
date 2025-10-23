# colleccion de elementos indexados, no ordeandos, y se puede modificar
# se forma con key-value

animales = {"tiger": "tigre", "whale": "ballena", "bird": "pajaro"}

print(animales)

# Acceder a un elemento particular con la key
print(animales["bird"])
print(animales.get("bird", "Not in dict"))
print(animales.get("dog", "Not in dict"))

# Añaadir un elemento
animales["cat"] = "gato"
animales["cow"] = "vaca"
animales["parrot"] = "loro"

print(animales)

# Borrar un elemento
animales.pop("bird")

print(animales)

# o con el metodo del
del animales["cat"]
print(animales)

# Acceder a los valores
for animal in animales:
    print(animal)
    
# Acceder a key y values
for key, value in animales.items():
    print(key, "-", value) 