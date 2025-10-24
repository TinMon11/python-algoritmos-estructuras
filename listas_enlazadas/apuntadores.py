# En una lista ciruclar, es conveniente tener apuntadores para saver donde empieza y donde termina la lista (cabeza y cola)


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.previous_node = None


node1 = Node(10)
node2 = Node(25)
node3 = Node(35)

# Enlace 1 con 2
node1.next_node = node2
node2.previous_node = node1

# Enlace 2 con 3
node2.next_node = node3
node3.previous_node = node2

# Enlace 1 con 3 (primero y ultimo)
node3.next_node = node1
node1.previous_node = node3

# Acceder a nod3 desde 1
print("Nodo 1 desde 3:", node3.next_node.value)
print("Nodo 3 desde 1:", node1.previous_node.value)

# Dar toda la vuelta
print("VUelta entera desde el 1:", node1.next_node.next_node.next_node.value)

#  Apuntadores
cabeza = node1
cola = node3

# Si queremos ir a la cabeza desde la cola
print("Cabeza desde apuntador cola:", cola.next_node.value)

# Si queremos ir a la cola desde cabeza
print("Cola desde cabeza:", cabeza.previous_node.value)