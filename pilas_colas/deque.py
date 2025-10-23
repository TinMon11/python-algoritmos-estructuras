# Mezcla entre Pila y Cola
# Podes insertar o remover tanto del inicio como del final, no del medio. Es como LIFO y FIFO junto... LFIFO

# Es una lista pero con sistema FIFO (primero en llegar, primero en salir) (LIFO son las pilas)


class Deque:
    # Constructor '__init__(self)'
    def __init__(self):
        self.elementos = []

    def estaVacio(self):
        return self.elementos == []

    def insertarCabeza(self, elemento):
        return self.elementos.append(elemento)

    def insertarCola(self, elemento):
        return self.elementos.insert(0, elemento)

    def eliminarCola(self):
        return self.elementos.pop(0)

    def eliminarCabeza(self):
        return self.elementos.pop()

    def consultarCabeza(self):
        ultimo_elemento = len(self.elementos)
        return self.elementos[ultimo_elemento - 1]

    def consultarCola(self):
        return self.elementos[0]

    def tamano(self):
        # Longitud de la cola
        return len(self.elementos)


d = Deque()

d.insertarCabeza("Verde")
d.insertarCabeza("Azul")
d.insertarCola("Rojo")
d.insertarCola("Naranja")

print("Longitud", d.tamano())

print("Cabeza Actual", d.consultarCabeza())
print("Cola Actual", d.consultarCola())

d.eliminarCola()
print("COLA LUEGO DE ELMINAR ANTERIOR COLA", d.consultarCola())

d.eliminarCabeza()

print("CABEZA LUEGO DE ELIMINAR CABEZA", d.consultarCabeza())
