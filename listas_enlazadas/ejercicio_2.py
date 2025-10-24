# En este ejercicio, deberás implementar una lista doblemente enlazada en Python. Una lista doblemente enlazada es una estructura de datos donde cada nodo tiene tres partes:
# Un valor (o dato).
# Una referencia al siguiente nodo (siguiente).
# Una referencia al nodo anterior (anterior).
# Requisitos
# Debes crear una clase Nodo que represente un nodo de la lista y una clase ListaDobleEnlazada que represente la lista. La clase ListaDobleEnlazada debe tener los siguientes métodos:
# insertar_inicio(valor): Inserta un nuevo nodo al inicio de la lista con el valor dado.
# insertar_final(valor): Inserta un nuevo nodo al final de la lista con el valor dado.
# eliminar(valor): Elimina el primer nodo que contiene el valor dado.
# buscar(valor): Busca si un nodo con el valor dado existe en la lista. Devuelve True si se encuentra, o False si no.
# mostrar_lista(): Devuelve una representación de la lista como una cadena de texto, mostrando todos los valores de los nodos de principio a fin.
# Además, también puedes agregar los siguientes métodos opcionalesz
# invertir_lista(): Invierte el orden de los nodos en la lista.
# mostrar_lista_invertida(): Muestra la lista en orden invertido.
# Métodos a implementar:
# class Nodo: Representa un nodo de la lista, que contiene un valor y enlaces tanto al siguiente nodo como al nodo anterior.
# class ListaDobleEnlazada: Representa la lista doblemente enlazada y tiene métodos para insertar, eliminar, buscar y mostrar los elementos.


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None


class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo

    def insertar_final(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

    def eliminar(self, valor):
        if self.cabeza is None:
            return  # lista vacía

        # Si el valor está en la cabeza
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            if self.cabeza is not None:
                self.cabeza.anterior = None
            else:
                self.cola = None  # lista vacía
            return

        actual = self.cabeza
        while actual is not None and actual.valor != valor:
            actual = actual.siguiente

        if actual is None:
            return  # valor no encontrado

        # Si es el último nodo
        if actual == self.cola:
            self.cola = actual.anterior
            self.cola.siguiente = None
        else:
            # Nodo en el medio
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior

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
        return " <-> ".join(elementos)

    def mostrar_lista_invertida(self):
        elementos = []
        actual = self.cola
        while actual is not None:
            elementos.append(str(actual.valor))
            actual = actual.anterior
        return " <-> ".join(elementos)

    def invertir_lista(self):
        actual = self.cabeza
        anterior = None
        while actual is not None:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            actual.anterior = siguiente
            anterior = actual
            actual = siguiente
        # intercambiamos cabeza y cola
        self.cabeza, self.cola = self.cola, self.cabeza


# ---------------------------
# Ejemplo de uso
# ---------------------------

lista = ListaDobleEnlazada()

lista.insertar_final("rojo")
lista.insertar_final("verde")
lista.insertar_final("azul")
print(lista.mostrar_lista())  # rojo -> verde -> azul

lista.insertar_inicio("amarillo")
print(lista.mostrar_lista())  # amarillo -> rojo -> verde -> azul

lista.eliminar("verde")
print(lista.mostrar_lista())  # amarillo -> rojo -> azul

print(lista.buscar("azul"))  # True
print(lista.buscar("negro"))  # False

print("Invertida:", lista.mostrar_lista_invertida())  # azul -> rojo -> amarillo
