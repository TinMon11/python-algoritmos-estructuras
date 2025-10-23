class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return True if len(self.items) == 0 else False

    def encolar(self, elemento):
        return self.items.append(elemento)

    def desencolar(self):
        return self.items.pop(0)

    def ver_frente(self):
        return self.items[0]


def operaciones_con_cola():
    # Crear una cola
    cola = Cola()

    # Encolar elementos en la cola
    cola.encolar(1)
    cola.encolar(2)
    cola.encolar(3)

    # Verificar si la cola está vacía
    esta_vacia = cola.esta_vacia()

    # Desencolar un elemento de la cola
    elemento_desencolado = cola.desencolar()

    # Ver el elemento en el frente de la cola
    elemento_en_el_frente = cola.ver_frente()

    # Devolver un diccionario con los resultados
    resultados = {
        "Cola está vacía": esta_vacia,
        "Elemento desencolado": elemento_desencolado,
    }
    return resultados


# Ejemplo de uso
resultados = operaciones_con_cola()
print("Resultados:")
print(resultados)
