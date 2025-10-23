# Dada una secuencia de números enteros, queremos encontrar el primer número que aparece más de una vez utilizando una pila y un conjunto.

# Objetivo
# Escribe una función que reciba una lista de números enteros y devuelva el primer número que aparece más de una vez en la secuencia. Si no hay ningún número repetido, devuelve None.

# Reglas
# Usa una pila para recorrer los números.
# Usa un conjunto para almacenar los números que ya se han visto, ya que los conjuntos permiten una búsqueda eficiente para saber si un número ya ha sido encontrado.
# La función debe devolver el primer número que aparece más de una vez.
# Si no hay números repetidos, la función debe devolver None.
# Método
# primer_repetido(lista): Recibe una lista de números enteros y devuelve el primer número que aparece más de una vez. Si no existe tal número, devuelve None.

# Ejemplo de Entrada y Salida
# Entrada:
# secuencia = [1, 2, 3, 4, 5, 3, 6, 7]
# Salida:
# 3


def primer_repetido(lista):
    conjunto = {}

    for numero in lista:
        conjunto[numero] = conjunto.get(numero, 0) + 1
        if conjunto[numero] > 1:
            return numero
    return None


print(primer_repetido([1, 2, 3, 4, 5, 2, 3, 6, 7]))
