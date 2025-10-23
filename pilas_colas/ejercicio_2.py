# Crear una clase que implementa la estrucutra de datos de una cola, utilizando 2 pilas
# Una cola mantiene el orden de los elementos (FIFO)
# Una pila cambia el orden (LIFO)


class Cola:
    def __init__(self):
        self.entrada = []
        self.salida = []

    def insertar(self, elemento):
        self.entrada.append(elemento)

    def eliminar(self):
        if not self.salida:
            while self.entrada:
                self.salida.append(self.entrada.pop())
        return self.salida.pop()

    def mostrar_salida(self):
        return self.salida

    def mostrar_entrada(self):
        return self.entrada


cola = Cola()

cola.insertar(1)
cola.insertar(2)
cola.insertar(3)
cola.insertar(4)

print("Salida", cola.mostrar_salida())
print("Entrada", cola.mostrar_entrada())


cola.eliminar()
cola.insertar(5)

print("Salida", cola.mostrar_salida())
print("Entrada", cola.mostrar_entrada())

cola.eliminar()

print("Salida", cola.mostrar_salida())
print("Entrada", cola.mostrar_entrada())
