# Es igual a la doblemente enalzada, pero a su vez hay enlace entre principio y final
# en el ejmplo de doblemente, es como si el nodo3 estuviera engahcnado al 1, y el 1 al 3 tambien


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
