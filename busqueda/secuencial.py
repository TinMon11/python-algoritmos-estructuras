# Busuqeda secuencial
# Va uno por uno en la lista.
# Metodo mas basico


def busqueda_secuencial(lista, elemento):
    posicion = 0
    encontrado = False

    while posicion < len(lista) and not encontrado:
        if lista[posicion] == elemento:
            encontrado = True

        posicion += 1
    return encontrado


print(busqueda_secuencial([1, 2, 5, 7, 2, 4], 50))
