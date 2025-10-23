class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        if not self.items:
            return True
        return False

    def apilar(self, elemento):
        return self.items.append(elemento)

    def desapilar(self):
        return self.items.pop()

    def ver_tope(self):
        last = len(self.items)
        if last > 0:
            return self.items[last - 1]
        else:
            return None


def operaciones_con_pila():
    # Crear una pila
    pila = Pila()

    # Apilar elementos en la pila
    pila.apilar(1)
    pila.apilar(2)
    pila.apilar(3)

    # Verificar si la pila está vacía
    esta_vacia = pila.esta_vacia()

    # Desapilar un elemento de la pila
    elemento_desapilado = pila.desapilar()

    # Ver el elemento en la cima de la pila
    elemento_en_la_cima = pila.ver_tope()

    # Devolver un diccionario con los resultados
    resultados = {
        "Pila está vacía": esta_vacia,
        "Elemento desapilado": elemento_desapilado,
        "Elemento en la cima": elemento_en_la_cima,
    }
    return resultados


# Ejemplo de uso
resultados = operaciones_con_pila()
print("Resultados:")
print(resultados)
