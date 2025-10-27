# Problema de maximizar ganancia en acciones
# Tienes una lista de precios de una acción, donde cada posición de la lista representa el precio de la acción en un momento específico del día.
# Tu objetivo es determinar la mayor ganancia posible que se puede obtener comprando una vez y vendiendo una vez.
# Condiciones
# Solo se puede comprar y vender una vez.
# No se puede vender antes de comprar.

# Ejemplo:

# precios = [7, 1, 5, 3, 6, 4]
# Compra al precio 1, vende al precio 6 → ganancia máxima = 5

precios = [24,20,14,11]


def maximizas(lista):
    if len(lista) < 2:
        raise Exception("Se necesitan al menos 2 valores en la lista")

    min_precio = lista[0]
    max_beneficio = lista[1] - lista[0]

    for precio in lista[1:]:
        beneficio = precio - min_precio
        max_beneficio = max(max_beneficio, beneficio)
        min_precio = min(min_precio, precio)
        
    return max_beneficio

print("Max Beneficio", maximizas(precios))