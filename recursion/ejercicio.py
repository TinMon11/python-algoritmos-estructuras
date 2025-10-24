# Escribe una función recursiva que recorra una lista de números y calcule la suma de todos sus elementos.
# La función debe seguir los siguientes pasos:
# Si la lista está vacía, debe devolver 0.
# Si la lista no está vacía, debe tomar el primer elemento de la lista y sumarlo al resultado de llamar recursivamente a la función con el resto de la lista.
# Requisitos:
# Implementa la función sumar_lista(lista), que tome una lista de números como argumento y devuelva la suma de todos los elementos de la lista usando recursión.
# Ejemplo de uso
# # Ejemplo de uso
# lista = [1, 2, 3, 4, 5]
# print(sumar_lista(lista))  # Debería devolver 15
# lista_vacia = []
# print(sumar_lista(lista_vacia))  # Debería devolver 0


# lista = [1, 2, 3, 4, 6]  # -> 16
lista = []  # -> 0


def sumar_lista(lista):
    if len(lista) == 0:
        return 0
    
    return lista[0] + sumar_lista(lista[1:])


print(sumar_lista(lista))
