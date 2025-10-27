# Si estan ordenados los datos, buscamos el valor hata enocntrarlo o hasta que el elemento de la lista sea mayor a lbuscado


def busqueda(lista, elemento):
    posicion = 0
    encontrada = False
    parar = False

    while posicion < len(lista) and not encontrada and not parar:
        print("Valor actual", lista[posicion])
        if lista[posicion] == elemento:
            encontrada = True
            parar = True

        if lista[posicion] > elemento:
            parar = True

        posicion += 1

    return encontrada


print(busqueda([1, 2, 3, 5, 7, 8, 12, 15], 11))
