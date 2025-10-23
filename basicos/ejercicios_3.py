# Consturir una clase Duplicados con una funcion 'contiene_duplicados'
# Dado un array de numeros, devolver True si hay duplicados, False si no.
# [1,2,5,6,7] -> False // [1,2,3,4,1] -> True


class Duplicados:
    def contiene_duplicados(self, numeros):

        conjunto = set(numeros)

        if len(conjunto) != len(numeros):
            return True
        return False


# d = Duplicados()
# print(d.contiene_duplicados([1, 2, 3, 5, 7, 1]))

# Crear una clase con una funcion
# REcibe un listado de numeros por parametro y un objetivo k
# Devolver los indices de cada par de numeros que sumen k
# Ejemplo -> [1, 3, 4,2] k = 5 -> [0, 2] [1, 3]
# Ejemplo -> [1, 6, 4,2,] k = 8 -> [1, 2]


class Suma_numero:
    def get_index(self, numeros, k):

        hash_map = {}
        resultado = set()
        for indice, value in enumerate(numeros):
            faltan = k - value
            if faltan in hash_map:
                resultado.add(
                    (
                        min(hash_map.get(faltan), indice),
                        max(hash_map.get(faltan), indice),
                    )
                )
            else:
                hash_map[value] = indice

        return resultado


clase = Suma_numero()

print(clase.get_index([1, 2, 3, 5, 6, 1], 8))
