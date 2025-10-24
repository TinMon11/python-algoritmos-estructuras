# Doblemente enlazada
# Los nodos no solo estan enlazadas hacia adelante, sino tambien hacia atras


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.previous_node = None


node1 = Node(10)
node2 = Node(25)
node3 = Node(35)

node1.next_node = node2

node2.previous_node = node1
node2.next_node = node3

node3.previous_node = node2

print("Nodo 1 Valor:", node1.value)
print("Node 2 Valor", node2.value)
print("Nodo 2 value accediendo desde el nodo 1:", node1.next_node.value)

print("Nodo previo al 3 Value (accediendo desde el 3):", node3.previous_node.value)

print("Valor del 3, pero accediendo desde el 1 al y 2 al 3: ", node1.next_node.next_node.value)