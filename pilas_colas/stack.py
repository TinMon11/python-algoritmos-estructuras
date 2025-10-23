# Es una lista, con sistema LIFO (last in first out)


class Pila:
    # Constructor '__init__(self)'
    def __init__(self):
        self.elementos = []

    def estaVacio(self):
        return self.elementos == []

    def insertar(self, elemento):
        return self.elementos.append(elemento)

    def eliminar(self):
        # Elimina el ultimo elemento
        return self.elementos.pop()

    def consultar_ultimo(self):
        # Cual es el ultimo de la pila
        ultimo_elemento = len(self.elementos)
        return self.elementos[ultimo_elemento - 1]

    def tamano(self):
        # Longitud de la pila
        return len(self.elementos)


p = Pila()

p.insertar("Verde")
p.insertar("Azul")
p.insertar("Rojo")

print("Pila Ultimo", p.consultar_ultimo())
print(p.tamano())

print("Esta vacia", p.estaVacio())
p.eliminar()

print("Pila Ultimo ahora", p.consultar_ultimo())

p.insertar("Naranja")

print("Pila Ultimo ahora 2", p.consultar_ultimo())