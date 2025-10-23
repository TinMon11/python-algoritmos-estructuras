# Una palabra es anagrama de otra
# Misma cantidad de letras y veces, pero en distinto orden
def is_anagrama(string1, string2):
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    if string1 == string2:
        return False

    if len(string1) != len(string2):
        return False

    contador = {}

    for letra in string1:
        contador[letra] = contador.get(letra, 0) + 1

    for letra in string2:
        contador[letra] = contador.get(letra, 0) - 1

    for letra in contador:
        if contador[letra] != 0:
            return False

    return True

    # Otra forma mas directa. Armo dos sets y calculo la differencia
    # string_1_set = set(string1)
    # string_2_set = set(string2)

    # result = string_1_set.difference(string_2_set)
    # if len(result) == 0:
    #     return True


# print(is_anagrama("Paris", "Prisa"))

# Suma de pares de numeros
# Dada una lista de numeros, mostrar que pares de numeros suman un valor k pasado por parametro
# Mostrar los pares de numeros y devolver la cantidad de pares d enumeros q usman ese valor k
# Ejemplo: [1,3,2,2] - k =4 -> (1,3) (2,2)


def suma_pares(numeros, k):
    vistos = set()
    result = set()
    for numero in numeros:
        faltan = k - numero
        if faltan not in vistos:
            vistos.add(numero)
        else:
            result.add((min(faltan, numero), max(faltan, numero)))

    print("Result", result)
    print("Length", len(result))


# suma_pares([1, 3, 2, 2, 5, 4, 6, 6], 7)

# Dada una lista de positivos y negativos
# Encontrar la suma continua de mayor valor
# Ejemplo: [4,6,8,-3,2,5,6,7] ->


def maxima_suma_continua(numeros):
    if len(numeros) == 0:
        return 0

    maximo = numeros[0]
    suma = numeros[0]

    for numero in numeros[1:]:
        suma = max(suma + numero, numero)
        maximo = max(suma, maximo)

    return maximo


# maxima_suma_continua([4, 6, 8, -3, 2, -5, 1])


class Probar_maximo_suma_continua(object):
    def prueba1(self):
        assert maxima_suma_continua([4, 6, 8, -3, 2, -5, 1]) == 18
        assert maxima_suma_continua([1, 5, -2, 4, -3, 2]) == 8
        assert maxima_suma_continua([3, -2, 6, 2, -3, 2]) == 9
        print("Succesfull tests")


testing = Probar_maximo_suma_continua()

testing.prueba1()
