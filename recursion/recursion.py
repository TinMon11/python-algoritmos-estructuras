# Una funcion hace una o mas llamadas a sí misma

# Ejercicio - Crear una funcion recursiva que pasado un numero, calcule la suma desde 0 hasta ese numero (incluido)


def suma(numero):
    if numero == 0:
        return 0
    return numero + suma(numero - 1)


print("Resultado", suma(7))

# Ejercicio , dar vuelta una cadena usando recursion
# Ejepmlo 'abcd' -> 'dcba'


def invertir(cadena: str):
    if len(cadena) == 1:
        return cadena
    return invertir(cadena[1:]) + cadena[0]


print("Inversion", invertir("abcde"))

# abcde -> reves(bcde) + a -> edcba
# reves(bcde) -> reves(cde) + b  -> edcb
# reves(cde) -> reves(de) + c -> edc
# reves(de) -> reves(d) + d -> ed
# reves(e) -> e