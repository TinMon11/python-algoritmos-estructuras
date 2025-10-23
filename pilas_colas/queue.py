# Es una lista pero con sistema FIFO (primero en llegar, primero en salir) (LIFO son las pilas)


class Cola:
    # Constructor '__init__(self)'
    def __init__(self):
        self.elementos = []

    def estaVacio(self):
        return self.elementos == []

    def insertar(self, elemento):
        # Insertamos el elemento adelante del todo
        # Porque dsps cuando 'sacamos' sacamos el de arriba del todo
        return self.elementos.insert(0, elemento)

    def eliminar(self):
        # Elimina el ultimo elemento (que fue el primero en entrar, xq voy meitneod adelante en el insert)
        return self.elementos.pop()

    def consultar_proximo(self):
        # Cual es el ultimo de la cola (que fue el primero que se agregó)
        ultimo_elemento = len(self.elementos)
        return self.elementos[ultimo_elemento - 1]

    def tamano(self):
        # Longitud de la cola
        return len(self.elementos)


c = Cola()

c.insertar("Verde")
c.insertar("Azul")
c.insertar("Rojo")

print("Cola Proximo en salir", c.consultar_proximo())
print(c.tamano())

print("Esta vacia", c.estaVacio())
c.eliminar()

print("Cola Proximo ahora", c.consultar_proximo())

c.insertar("Naranja")
c.eliminar()

print("Cola Proximo ahora 2", c.consultar_proximo())
