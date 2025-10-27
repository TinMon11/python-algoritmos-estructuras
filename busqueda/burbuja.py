# Ordena los elementos "cambiandolos" de lugar (uno para adelante, el otro para atras, a medida q lo va recorriendo).
# El método de ordenamiento burbuja compara elementos vecinos y los intercambia si están en el orden incorrecto, repitiendo el proceso hasta que la lista queda ordenada.


def ordenar(lista):
    for numero in range(len(lista) - 1, 0, -1):
        for indice in range(numero):
            if lista[indice] > lista[indice + 1]:
                temporal = lista[indice]
                lista[indice] = lista[indice + 1]
                lista[indice + 1] = temporal


lista = [1, 5, 4, 12, 6, 8, 9, 11]
ordenar(lista)

print("Lista Ordenada", lista)
