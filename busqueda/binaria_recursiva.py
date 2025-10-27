def busqueda_recursiva_binaria(lista, elemento):

    if len(lista) == 0:
        return False
    else:
        medio = len(lista) // 2

        if lista[medio] == elemento:
            return True

        else:
            if lista[medio] > elemento:
                return busqueda_recursiva_binaria(lista[:medio], elemento)
            else:
                return busqueda_recursiva_binaria(lista[medio:], elemento)


print(busqueda_recursiva_binaria([1, 2, 5, 6, 7, 12, 15, 17, 33], 12))
