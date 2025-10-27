def ordenar(lista):
    # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(lista) <= 1:
        return

    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]

    # Ordenamos recursivamente cada mitad
    ordenar(izquierda)
    ordenar(derecha)

    i, j, k = 0, 0, 0

    # Mezclamos izquierda y derecha en orden ascendente
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            lista[k] = izquierda[i]
            i += 1
        else:
            lista[k] = derecha[j]
            j += 1
        k += 1

    # Agregamos los elementos restantes
    while i < len(izquierda):
        lista[k] = izquierda[i]
        i += 1
        k += 1

    while j < len(derecha):
        lista[k] = derecha[j]
        j += 1
        k += 1


# Ejemplo
lista = [19, 22, 7, 3, 15, 8, 10]
ordenar(lista)

print("LISTA ORDENADA", lista)