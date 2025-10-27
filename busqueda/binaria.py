# En una busqueda binaria de una lista ordenada, empezas a buscar por el medio de la lista, y ves si vas hacia adelante o atras dependiendo si es mayor o menor al buscado


def busqueda(lista, elemento):
    primero = 0
    ultimo = len(lista) - 1
    encontrado = False

    while primero <= ultimo and not encontrado:
        medio = (primero + ultimo) // 2
        print(
            f"Primero: {lista[primero]}, Último: {lista[ultimo]}, Medio: {lista[medio]}"
        )

        if lista[medio] == elemento:
            encontrado = True
            print(f"¡Elemento {elemento} encontrado en la posición {medio}!")

        else:
            if elemento < lista[medio]:
                print(f"{elemento} es menor que {lista[medio]}, busco a la izquierda")
                ultimo = medio - 1
            else:
                print(f"{elemento} es mayor que {lista[medio]}, busco a la derecha")
                primero = medio + 1

    if not encontrado:
        print(f"Elemento {elemento} no encontrado en la lista.")
    return encontrado


print(busqueda([1, 2, 3, 4, 6, 8, 9, 12, 17, 19], 9))
