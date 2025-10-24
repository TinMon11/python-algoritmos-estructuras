# Construir la funcion es_ciruclar que verifique, tomando un nodo como parametro, si una lista es circular o no
# Construir una lista ciruclar y otra no ciruclar para hacer la pruebas
# Crear una clase de test par ahcaer las pruebas

# Ejemplos
# (Nodo1 -> Nodo2 -> Nodo3 -> Nodo1) es True
# (Nodo1 -> Nodo2 -> Nodo3) -> False


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.previous_node = None


def es_circular(nodo: Node):
    marcador1 = nodo
    marcador2 = nodo

    i = 1
    while marcador2 != None and marcador2.next_node != None:
        print("**********************")
        print("ITERACION NUMERO:", i)
        marcador1 = marcador1.next_node
        marcador2 = marcador2.next_node.next_node

        print("Marcador 1 Ahora es:", marcador1.value)
        print("Marcador 2 Ahora es:", marcador2.value)

        if marcador1 == marcador2:
            return True
    return False


# Lista ciruclar para testing
node1 = Node("nodo1")
node2 = Node("nodo2")
node3 = Node("nodo3")
node4 = Node("nodo4")

node1.next_node = node2
node2.next_node = node3
node3.next_node = node4
node4.next_node = node1

# Lista no circular
node7 = Node("nodo7")
node8 = Node("nodo8")
node9 = Node("nodo9")
node10 = Node("nodo10")

node7.next_node = node8
node8.next_node = node9
node9.next_node = node10


class Pruebas:
    def run_test(self):
        assert (es_circular(node3)) == True
        assert es_circular(node8) == False

        print("Succesfull test")
        
pruebas = Pruebas()

pruebas.run_test()
