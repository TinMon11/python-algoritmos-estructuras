# En este ejercicio, deberás implementar una lista simplemente enlazada en Python. Una lista simplemente enlazada es una estructura de datos en la que cada elemento (o nodo) contiene dos partes:

# Requisitos
# Debes crear una clase Nodo que represente un nodo de la lista y una clase ListaEnlazada que represente la lista. La clase ListaEnlazada debe tener los siguientes métodos:
# insertar_inicio(valor): Inserta un nuevo nodo al inicio de la lista con el valor dado.
# insertar_final(valor): Inserta un nuevo nodo al final de la lista con el valor dado.
# eliminar(valor): Elimina el primer nodo que contiene el valor dado.
# buscar(valor): Busca si un nodo con el valor dado existe en la lista. Devuelve True si se encuentra, o False si no.
# mostrar_lista(): Devuelve una representación de la lista como una cadena de texto, mostrando todos los valores de los nodos de principio a fin.

# Métodos a implementar:
# class Nodo: Representa un nodo de la lista, que contiene un valor y un enlace al siguiente nodo.
# class ListaEnlazada: Representa la lista enlazada y tiene métodos para insertar, eliminar, buscar y mostrar los elementos.

# Consideraciones:
# La implementación debe permitir que la lista se modifique dinámicamente.
# Debes manejar casos especiales, como:
# Intentar eliminar un valor que no existe en la lista.
# Intentar buscar un valor en una lista vacía.
# Insertar en una lista vacía.

# Objetivo:
# Este ejercicio te ayudará a comprender cómo funciona una lista simplemente enlazada, cómo manipular nodos y cómo navegar por la lista para insertar, eliminar y buscar elementos.


# Clase Nodo: representa un elemento de la lista
# Clase Nodo: representa un elemento de la lista
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


# Clase ListaEnlazada: gestiona los nodos
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Primer nodo
        self.cola = None  # Último nodo (para insertar al final más fácil)

    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        # Si la lista está vacía, cabeza y cola apuntan al nuevo nodo
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo

    def insertar_final(self, valor):
        nuevo = Nodo(valor)
        # Si la lista está vacía
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            self.cola = nuevo

    def eliminar(self, valor):
        if self.cabeza is None:
            return  # lista vacía, no hace nada

        # Si el valor está en la cabeza
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            if self.cabeza is None:
                self.cola = None
            return

        # Buscar el valor en el resto de la lista
        actual = self.cabeza
        while actual.siguiente is not None and actual.siguiente.valor != valor:
            actual = actual.siguiente

        # Si no se encontró el valor
        if actual.siguiente is None:
            return

        # Eliminar el nodo
        actual.siguiente = actual.siguiente.siguiente

        # Si eliminamos el último nodo, actualizamos la cola
        if actual.siguiente is None:
            self.cola = actual

    def buscar(self, valor):
        actual = self.cabeza
        while actual is not None:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def mostrar_lista(self):
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(str(actual.valor))
            actual = actual.siguiente
        # Si la lista está vacía, devolver cadena vacía ("")
        return " -> ".join(elementos)

    def lista_vacia(self):
        return self.cabeza is None


# ---------------------------
# Ejemplo de uso
# ---------------------------

lista = ListaEnlazada()

print("Vacia", lista.lista_vacia())
lista.insertar_final("rojo")
lista.insertar_final("verde")
lista.insertar_final("azul")
print(lista.mostrar_lista())  # rojo -> verde -> azul
lista.insertar_inicio("naranja")
print(lista.mostrar_lista())  # naranja -> rojo -> verde -> azul

lista.insertar_inicio("amarillo")
print(lista.mostrar_lista())  # amarillo -> naranja -> rojo -> verde -> azul

lista.eliminar("verde")
print(lista.mostrar_lista())  # amarillo -> naranja -> rojo -> azul

print(lista.buscar("azul"))  # True
print(lista.buscar("negro"))  # False

print("Vacia", lista.lista_vacia())
