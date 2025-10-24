# Son listas que tienen un valor, y a su vez un pointer al nodo siguiente

class Node:
    def __init__(self, valor):
        self.value = valor
        self.next_node = None


node1 = Node(10)
node2 = Node(25)
node3 = Node(35)

print("Node 1", node1.value)
print("Node 1", node1.next_node)

# Enalzar con el siguiente nodo
node1.next_node = node2
node2.next_node = node3

print("Node 2", node2.value)
print("Node 2", node2.next_node.value)