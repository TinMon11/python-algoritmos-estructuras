# En el método de selección, en cada recorrido se busca el elemento más pequeño (o el más grande, según el orden) y se coloca en su posición correcta de la lista.

# Lista = [6,5,4,1,8,7,2,4]
# Primer vuelta
# ---> Maximo 8 --> Lo intercambio con el 4 (el ultimo de la lista) -> 65414728
# Segunda vuelta (comparo hasta el anteultimo numero, ya que el ultio es el mas grande xq lo pusmos antes)
# --> Maximo 7 -> intercambio con el 2 (porque va a ir ahi) -> 65414278
# Tercer vuelta (comparo hasta el anterior del 7 q pusimos recien)
# Maximo 6 -> intercambio con el 2 -> 25414678


def ordenar(lista):
    for numero in range(len(lista) - 1, 0, -1):
        indiceMax = 0
        for indice in range(1, numero + 1):
            if lista[indice] > lista[indiceMax]:
                indiceMax = indice
        temporal = lista[numero]
        lista[numero] = lista[indiceMax]
        lista[indiceMax] = temporal


lista = [1, 5, 4, 12, 6, 8, 9, 11]
ordenar(lista)

print("Lista Ordenada", lista)
