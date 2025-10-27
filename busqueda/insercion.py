# El método de inserción toma cada elemento (uno por uno) y lo inserta en el lugar correcto dentro de la parte ya ordenada de la lista.
# Es como cuando ordenás cartas en la mano:
# Empezás con una carta (ya está ordenada).
# Agarrás la siguiente y la metés donde corresponde.
# Repetís hasta que todas estén en su lugar.


def ordenar(lista):

    for indice in range(1, len(lista)):
        valor = lista[indice]
        posicion = indice

        while posicion > 0 and lista[posicion - 1] > valor:
            lista[posicion] = lista[posicion - 1]
            posicion -= 1

        lista[posicion] = valor


lista = [1, 5, 4, 12, 6, 8, 9, 11]
ordenar(lista)

print("Lista Ordenada", lista)

def ordenar_con_debugging(lista):
    print("Lista inicial:", lista)
    print("-" * 40)
    for indice in range(1, len(lista)):
        valor = lista[indice]
        posicion = indice
        print(f"Iteración {indice}: tomamos valor = {valor} (posición inicial {indice})")

        # mostrar la "zona ordenada" antes del insert
        print("  Zona ordenada previa:", lista[:indice])

        # desplazamientos hacia la derecha
        while posicion > 0 and lista[posicion - 1] > valor:
            print(f"    {lista[posicion-1]} > {valor} -> desplazo {lista[posicion-1]} a la posición {posicion}")
            lista[posicion] = lista[posicion - 1]
            posicion -= 1
            print("    Estado intermedio:", lista)

        # insertar el valor en la posición encontrada
        lista[posicion] = valor
        print(f"  Insertamos {valor} en la posición {posicion}")
        print("  Lista ahora:", lista)
        print("-" * 40)

    print("Lista ordenada final:", lista)


# ejemplo
lista = [1, 5, 4, 12, 6, 3, 9, 11]
ordenar_con_debugging(lista)

