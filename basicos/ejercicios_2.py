# Verificar que dos listas de numeros son iguales, que contienen los mismo valores (no importa el orden)
# Eejplmo [1, 2, 4, 5, 6] y [6, 5 ,4, 2, 1] son iguales
# Eejplmo [1, 2, 3,6,4] y [1,2,3,5,4] no son iguales


def list_are_equal(list1, list2):

    if len(list1) != len(list2):
        return False

    dict1 = {}

    for number in list1:
        dict1[number] = dict1.get(number, 0) + 1

    for number in list2:
        dict1[number] = dict1.get(number, 0) - 1

    for number in dict1:
        if dict1[number] != 0:
            return False

    return True

    # Otra opcion, ordenarlas e ir comparando uno por uno
    ordenada1 = sorted(list1)
    ordenada2 = sorted(list2)

    for num1, num2 in zip(ordenada1, ordenada2):
        if num1 != num2:
            return False

    return True


# print(list_are_equal([1, 2, 4, 5, 6], [6, 5, 4, 2, 1]))

# Ahora dadas dos listas, encontrar elementos que estan eun una ilsta pero no en la otra.
# Eejplmo [1, 2, 4, 5, "hola"] y [6, 5 ,4, 2, 1] -> "hola" y 6
# Eejplmo [1, 2, 4, 5, 6] y [7, 5 ,4, 2, "hola"] -> 6,7, hola


def diferencias(lista1, lista2):

    hash_map = {}
    diferencia = []

    for elemento in lista1:
        hash_map[elemento] = hash_map.get(elemento, 0) + 1

    for elemento in lista2:
        hash_map[elemento] = hash_map.get(elemento, 0) - 1

    for key, value in hash_map.items():
        if value != 0:
            diferencia.append(key)

    return diferencia


# print(diferencias([1, 2, 4, 5, "hola"], [6, 5, 4, 2, 1]))
# print(diferencias([1, 2, 4, 5, 6], [7, 5, 4, 2, "hola"]))


# Dada una cadenta de texto, comprimir en funcion de sus repeticiones
# Ejemplo "AABBBCCCCD"  -> A2B3C4D1
# "AAABDDEEEaa -> A3B1D2E3a2


def comprimir(cadena):

    hash_map = {}
    result = ""

    for letra in cadena:
        hash_map[letra] = hash_map.get(letra, 0) + 1

    for key, value in hash_map.items():
        result = result + str(key) + str(value)
        
    return result

print(comprimir("AAAABBCDDDDeeA"))
