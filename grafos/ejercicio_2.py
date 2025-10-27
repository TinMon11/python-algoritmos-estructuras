# Eres parte del equipo de ingeniería de una ciudad que debe optimizar su red de tuberías de agua potable. La ciudad está dividida en sectores (nodos), y cada sector puede estar conectado con otros mediante tuberías (aristas).
# Cada tubería tiene asociado:
# Costo de instalación o mantenimiento (en miles de dólares)
# Capacidad máxima de agua que puede transportar
# La ciudad quiere:
# ✅ Minimizar el costo total de la red mientras se garantiza la conexión entre todos los sectores.
# Tu tarea es:
# Modelar el sistema como un grafo no dirigido y ponderado.
# Usar el algoritmo de Kruskal para construir el Árbol de Expansión Mínima (MST) que una todos los sectores al menor costo posible.
# (Opcional) Verificar la capacidad mínima total de la red construida.
# 🛠 Conceptos que se practican:
# ✅ Grafos no dirigidos y ponderados
# ✅ Árbol de expansión mínima (Minimum Spanning Tree)
# ✅ Algoritmo de Kruskal
# ✅ Aplicación en diseño de infraestructuras reales

# Ejemplo de uso
# # 🔧 Datos de prueba (ejemplo de red de tuberías)
# nodos = ["A", "B", "C", "D", "E"]
# conexiones = [
#     (4, "A", "B"),
#     (3, "A", "C"),
#     (2, "B", "C"),
#     (5, "B", "D"),
#     (7, "C", "D"),
#     (8, "C", "E"),
#     (6, "D", "E")
# ]

# # 🟢 Ejecutamos Kruskal
# mst_resultado, costo_total = kruskal_mst(nodos, conexiones)

# # 📌 Mostramos el resultado
# print("Tuberías seleccionadas para la red:")
# for nodo1, nodo2, costo in mst_resultado:
#     print(f"{nodo1} - {nodo2} | Costo: ${costo}k")

# print(f"\nCosto total mínimo de la red: ${costo_total}k")


# Salida esperada

# Tuberías seleccionadas para la red:
# B - C | Costo: $2k
# A - C | Costo: $3k
# B - D | Costo: $5k
# D - E | Costo: $6k

# Costo total mínimo de la red: $16k
# 🌿 ¿Qué es un Árbol de Expansión Mínima (MST)?
# Es una subred de un grafo conectado y no dirigido que:
# ✅ Une todos los nodos
# ✅ No tiene ciclos
# ✅ Tiene el menor costo posible (suma de los pesos de las conexiones)

# Se usa en problemas como:
# Red de agua
# Red eléctrica
# Rede de fibra óptica
# Carreteras

# 🔧 Algoritmo de Kruskal
# Idea básica: Ir agregando las conexiones (aristas) más baratas que no formen ciclos hasta unir todos los nodos.
# 🔎 Pasos:
# Ordena todas las aristas de menor a mayor costo.
# Ve tomando las más baratas y agrégalas si no forman un ciclo.
# Repite hasta conectar todos los nodos.
# ✅ Ventaja:
# Ideal si la red tiene pocos nodos y muchas conexiones.

# 🔗 Kruskal: Piensa en armar la red por "puentes"
# Imagina que tienes un mapa y una lista de posibles tuberías con su costo.
# Ordenas las tuberías de la más barata a la más cara.
# Empiezas a colocar la más barata y sigues... solo si no haces un círculo (ciclo).
# Termias cuando todos los sectores están conectados.
# ✅ Lo bueno: Funciona muy bien si tienes muchos sectores pero no tantas conexiones posibles.
# ✅ Ideal para: Redes donde las conexiones son costosas y escasas (ej. unir islas con puentes).


# ----------------------------
# Estructura de datos Union-Find (para evitar ciclos)
# ----------------------------
class UnionFind:
    def __init__(self, nodos):
        self.padre = {nodo: nodo for nodo in nodos}
        self.rango = {nodo: 0 for nodo in nodos}

    def find(self, nodo):
        if self.padre[nodo] != nodo:
            self.padre[nodo] = self.find(self.padre[nodo])  # compresión de ruta
        return self.padre[nodo]

    def union(self, nodo1, nodo2):
        raiz1 = self.find(nodo1)
        raiz2 = self.find(nodo2)
        if raiz1 == raiz2:
            return False  # ya están conectados, no se hace unión
        # unir según rango
        if self.rango[raiz1] < self.rango[raiz2]:
            self.padre[raiz1] = raiz2
        elif self.rango[raiz1] > self.rango[raiz2]:
            self.padre[raiz2] = raiz1
        else:
            self.padre[raiz2] = raiz1
            self.rango[raiz1] += 1
        return True


# ----------------------------
# Algoritmo de Kruskal
# ----------------------------
def kruskal_mst(nodos, conexiones):
    # Ordenamos las aristas por costo
    aristas = sorted(conexiones, key=lambda x: x[0])
    uf = UnionFind(nodos)
    mst = []
    costo_total = 0

    for costo, nodo1, nodo2 in aristas:
        if uf.union(nodo1, nodo2):  # si no forma ciclo
            mst.append((nodo1, nodo2, costo))
            costo_total += costo

    return mst, costo_total


# ----------------------------
# Datos de prueba
# ----------------------------
nodos = ["A", "B", "C", "D", "E"]
conexiones = [
    (4, "A", "B"),
    (3, "A", "C"),
    (2, "B", "C"),
    (5, "B", "D"),
    (7, "C", "D"),
    (8, "C", "E"),
    (6, "D", "E"),
]

# ----------------------------
# Ejecutar Kruskal
# ----------------------------
mst_resultado, costo_total = kruskal_mst(nodos, conexiones)

# ----------------------------
# Mostrar resultados
# ----------------------------
print("Tuberías seleccionadas para la red:")
for nodo1, nodo2, costo in mst_resultado:
    print(f"{nodo1} - {nodo2} | Costo: ${costo}k")

print(f"\nCosto total mínimo de la red: ${costo_total}k")
