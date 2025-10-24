# Se pide implementar una lista circular simple en Python. Una lista circular es una lista enlazada en la que el último nodo apunta de nuevo al primer nodo, creando un ciclo.

# Requerimientos:
# Definir la clase Nodo:
# La clase Nodo debe contener los atributos valor y siguiente, siendo siguiente una referencia al siguiente nodo en la lista.
# Definir la clase ListaCircular:
# La clase ListaCircular debe contener los siguientes métodos:
# Métodos a implementar:
# insertar_inicio(valor): Inserta un nodo con el valor dado al inicio de la lista.
# insertar_final(valor): Inserta un nodo con el valor dado al final de la lista.
# eliminar(valor): Elimina el primer nodo que contiene el valor dado.
# buscar(valor): Busca un nodo con el valor dado en la lista.
# mostrar_lista(): Muestra los valores de los nodos de la lista circular en formato de cadena, comenzando desde la cabeza y mostrando cada valor, hasta que se complete el ciclo.
# contar_elementos(): Devuelve el número de nodos en la lista circular.
# Consideraciones:
# Si la lista está vacía, el primer nodo y el último nodo deben estar apuntando a None.
# Asegúrate de manejar correctamente los punteros siguiente para formar el ciclo, es decir, el último nodo debe apuntar de nuevo al primer nodo.


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaCircular:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza is None:
            # primer nodo: cabeza y cola apuntan al mismo nodo
            self.cabeza = nuevo
            self.cola = nuevo
            nuevo.siguiente = nuevo  # apunta a sí mismo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
            self.cola.siguiente = self.cabeza  # mantener el ciclo

    def insertar_final(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
            nuevo.siguiente = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.siguiente = self.cabeza
            self.cola = nuevo

    def eliminar(self, valor):
        if self.cabeza is None:
            return  # lista vacía

        actual = self.cabeza
        anterior = self.cola
        encontrado = False

        while True:
            if actual.valor == valor:
                encontrado = True
                break
            anterior = actual
            actual = actual.siguiente
            if actual == self.cabeza:
                break  # dimos la vuelta completa

        if not encontrado:
            return  # valor no encontrado

        # Si hay un solo nodo
        if self.cabeza == self.cola and actual == self.cabeza:
            self.cabeza = None
            self.cola = None
        else:
            anterior.siguiente = actual.siguiente
            # si eliminamos la cabeza
            if actual == self.cabeza:
                self.cabeza = actual.siguiente
            # si eliminamos la cola
            if actual == self.cola:
                self.cola = anterior

    def buscar(self, valor):
        if self.cabeza is None:
            return False

        actual = self.cabeza
        while True:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return False

    def mostrar_lista(self):
        if self.cabeza is None:
            return ""
        elementos = []
        actual = self.cabeza
        while True:
            elementos.append(str(actual.valor))
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return " -> ".join(elementos)

    def contar_elementos(self):
        if self.cabeza is None:
            return 0
        contador = 0
        actual = self.cabeza
        while True:
            contador += 1
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return contador


# ---------------------------
# Ejemplo de uso
# ---------------------------

lista = ListaCircular()

lista.insertar_final("rojo")
lista.insertar_final("verde")
lista.insertar_final("azul")
print(lista.mostrar_lista())  # rojo -> verde -> azul

lista.insertar_inicio("amarillo")
print(lista.mostrar_lista())  # amarillo -> rojo -> verde -> azul

lista.eliminar("verde")
print(lista.mostrar_lista())  # amarillo -> rojo -> azul

print(lista.buscar("azul"))   # True
print(lista.buscar("negro"))  # False

print("Cantidad de elementos:", lista.contar_elementos())  # 3

