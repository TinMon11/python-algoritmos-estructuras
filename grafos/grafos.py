# Un grafo es un conjunto de puntos llamados nodos (o vértices) conectados por líneas llamadas aristas (o enlaces).
# Se usa para representar relaciones entre cosas, como ciudades conectadas por rutas, amigos en una red social, o páginas web enlazadas.
# Los nodos pueden estar conectados o no, y las conexiones pueden tener dirección (unidireccional) o ser bidireccionales.
# Los grafos ayudan a modelar y resolver problemas de rutas, redes, dependencias y relaciones entre objetos.

# Una matriz de adyacencia es una forma de representar un grafo con una tabla.
# Se crea una tabla cuadrada, donde las filas y columnas son los nodos del grafo.
# Si hay una conexión entre dos nodos, se pone un 1 (o el peso de la arista), y si no, se pone un 0.
# Así se puede ver y procesar fácilmente qué nodos están conectados entre sí.

# Grafo no dirigido: las conexiones no tienen dirección, es decir, si A está conectado con B, B también está conectado con A. Se dibuja como una línea simple entre los nodos.
# Grafo dirigido: las conexiones tienen dirección, como flechas; si hay una flecha de A a B, no necesariamente hay de B a A.
# Grafo ponderado: las conexiones tienen un peso o costo, como la distancia entre ciudades o el tiempo que tarda ir de un nodo a otro.


class Vertice:
    def __init__(self, clave):
        self.id = clave
        self.conexiones = {}

    def incluirVecino(self, vecino, peso=0):
        self.conexiones[vecino] = peso
        return

    def verConexiones(self):
        return self.conexiones.keys()

    def verId(self):
        return self.id

    def verPeso(self, vecino):
        return self.conexiones[vecino]

    def __str__(self):
        # print
        return str(self.id) + " conectado con " + str([x for x in self.verConexiones()])


class Grafo:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def incluirVertices(self, clave):
        nuevoVertice = Vertice(clave)
        self.vertices[clave] = nuevoVertice
        self.numVertices += 1
        return nuevoVertice

    def verVertice(self, clave):
        if clave in self.vertices:
            return self.vertices[clave]

        return None

    def incluirArista(self, origen, destino, peso=0):
        if origen not in self.vertices:
            self.incluirVertices(origen)

        if destino not in self.vertices:
            self.incluirVertices(destino)

        self.vertices[origen].incluirVecino(destino, peso)

        return

    def verListaVertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())


# Ejecutarlo
grafo = Grafo()

grafo.incluirVertices(1)
grafo.incluirVertices(2)
grafo.incluirVertices(3)
grafo.incluirVertices(4)

print(grafo.verListaVertices())

grafo.incluirArista(1, 2, 4)  # Origen 1, destino 2, peso 4
grafo.incluirArista(1, 4, 2)
grafo.incluirArista(2, 4, 1)
grafo.incluirArista(2, 3, 1)

for vertice in grafo:
    print(vertice)  # Esto usa el __str__ de la clase Vertice
    for vecino in vertice.verConexiones():
        print(f"  {vertice.verId()} -> {vecino} (peso {vertice.verPeso(vecino)})")