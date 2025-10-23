# Descripción:
# Estás desarrollando un procesador de texto básico y necesitas implementar una funcionalidad de deshacer (undo) y rehacer (redo) utilizando pilas.

# Objetivo:
# Implementar una estructura que permita al usuario escribir texto, deshacer la última acción y rehacerla si es necesario.

# Instrucciones:
# Crea una clase EditorTexto con los siguientes métodos:
# escribir(texto: str): Agrega una nueva acción de escritura.
# deshacer(): Revierte la última acción y la guarda para poder rehacerla.
# rehacer(): Restaura la última acción deshecha.
# mostrar_contenido(): Devuelve el contenido actual del texto.

# Usa dos pilas para manejar las acciones:
# Una pila pila_undo para almacenar acciones realizadas.
# Una pila pila_redo para almacenar acciones deshechas y permitir rehacerlas.
# Simula una serie de operaciones como escribir palabras, deshacer y rehacer para validar el funcionamiento.


class EditorText:
    def __init__(self):
        self.pila1 = []
        self.pila2 = []

    def escribir(self, letra):
        return self.pila1.append(letra)

    def deshacer(self):
        if self.pila1:
            return self.pila2.append(self.pila1.pop())
        return

    def rehacer(self):
        if self.pila2:
            return self.pila1.append(self.pila2.pop())
        return

    def mostrar(self):
        return self.pila1


editor = EditorText()

editor.escribir("a")
editor.escribir("b")
editor.escribir("c")
editor.escribir("d")
print("Texto:", editor.mostrar())
editor.deshacer()
editor.deshacer()
print("Texto:", editor.mostrar())
editor.deshacer()
editor.deshacer()
editor.deshacer()
editor.deshacer()
editor.deshacer()
editor.deshacer()
print("Texto:", editor.mostrar())
editor.rehacer()
editor.rehacer()
print("Texto:", editor.mostrar())
editor.rehacer()
editor.rehacer()
editor.rehacer()
print("Texto:", editor.mostrar())
