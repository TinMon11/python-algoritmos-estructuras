# El algoritmo Shell es una mejora del método de inserción: compara y ordena elementos que están separados por una cierta “distancia” (gap).
# Esa distancia se va reduciendo progresivamente hasta llegar a 1, momento en el que la lista ya casi está ordenada y el algoritmo termina muy rápido.


def ordenar(lista):
    # Empezamos con un gap (distancia) igual a la mitad del largo de la lista
    sublistas = len(lista) // 2

    while sublistas > 0:
        # Recorremos cada sublista separada por el gap
        for inicio in range(sublistas):
            ordenacion_gap(lista, inicio, sublistas)

        # Reducimos el gap a la mitad en cada pasada
        sublistas = sublistas // 2


def ordenacion_gap(lista, inicio, gap):
    # Ordena usando inserción pero con elementos separados por "gap"
    for i in range(inicio + gap, len(lista), gap):
        valor_actual = lista[i]
        posicion = i

        # Mueve hacia adelante los elementos mayores al valor actual
        while posicion >= gap and lista[posicion - gap] > valor_actual:
            lista[posicion] = lista[posicion - gap]
            posicion -= gap

        lista[posicion] = valor_actual


# Ejemplo
lista = [19, 22, 7, 3, 15, 8, 10]
ordenar(lista)
print("Lista ordenada:", lista)
