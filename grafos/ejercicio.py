# Una aerolínea necesita un sistema de planificación de rutas que permita determinar la mejor conexión entre aeropuertos.
# Para esto, debes modelar la red de aeropuertos como un grafo dirigido ponderado, donde:
# Los nodos representan aeropuertos.
# Las aristas representan vuelos entre aeropuertos.
# El peso de cada arista es el tiempo de vuelo en minutos.
# Tu tarea es implementar un sistema que permita:
# Agregar aeropuertos y vuelos con tiempos de vuelo.
# Encontrar la ruta más corta entre dos aeropuertos usando el algoritmo de Dijkstra.
# Mostrar la mejor ruta y el tiempo total del viaje.

# Ejemplo de entrada:
# # Crear grafo
# red_aerea = GrafoVuelos()
# red_aerea.agregar_aeropuerto("Madrid")
# red_aerea.agregar_aeropuerto("París")
# red_aerea.agregar_aeropuerto("Londres")
# red_aerea.agregar_aeropuerto("Berlín")

# # Agregar vuelos (origen, destino, tiempo de vuelo en minutos)
# red_aerea.agregar_vuelo("Madrid", "París", 120)
# red_aerea.agregar_vuelo("Madrid", "Londres", 150)
# red_aerea.agregar_vuelo("París", "Berlín", 100)
# red_aerea.agregar_vuelo("Londres", "Berlín", 130)

# # Buscar la mejor ruta
# ruta, tiempo_total = red_aerea.ruta_mas_corta("Madrid", "Berlín")
# print(f"Mejor ruta: {ruta} con un tiempo total de {tiempo_total} minutos")

# Salida esperada:
# Mejor ruta: ['Madrid', 'París', 'Berlín'] con un tiempo total de 220 minutos

# El algoritmo de Dijkstra se usa para encontrar la ruta más corta desde un punto de partida hasta otros puntos en un grafo con pesos positivos (como tiempo de vuelo, distancia, costo, etc.).

# ¿Cómo funciona? 🛣️
# Marcamos el aeropuerto de origen con distancia 0 y todos los demás con "infinito" (porque aún no sabemos cómo llegar).
# Visitamos el aeropuerto con la menor distancia conocida.
# Actualizamos las distancias de los aeropuertos vecinos sumando la distancia actual + el tiempo del vuelo.
# Marcamos el aeropuerto como "visitado" para no volver a procesarlo.
# Repetimos hasta encontrar el destino o visitar todos los aeropuertos.
# Ejemplo práctico con aeropuertos ✈️
# Imagina que tenemos estos vuelos con tiempos en minutos:
# Madrid → París (120 min)
# Madrid → Londres (150 min)
# París → Berlín (100 min)
# Londres → Berlín (130 min)
# Queremos ir de Madrid a Berlín.

# 🔹 Paso 1: Inicializamos distancias
# Madrid = 0    (Punto de inicio)
# París = ∞
# Londres = ∞
# Berlín = ∞
# 🔹 Paso 2: Visitamos Madrid
# Desde Madrid, podemos ir a:
# París (120 min) → Actualizamos: París = 120
# Londres (150 min) → Actualizamos: Londres = 150
# 🔹 Paso 3: Visitamos París (la opción más corta)
# Desde París, podemos ir a:
# Berlín (100 min) → Actualizamos: Berlín = 120 + 100 = 220
# 🔹 Paso 4: Visitamos Londres
# Desde Londres, podemos ir a:
# Berlín (130 min) → Nueva distancia: 150 + 130 = 280 (NO es mejor que 220, así que lo ignoramos).
# 🔹 Paso 5: Visitamos Berlín
# Hemos llegado a Berlín en 220 minutos con la mejor ruta:
# Madrid → París → Berlín (220 min)

import math


class Aeropuerto:
    def __init__(self, clave):
        self.name = clave
        self.conexiones = {}

    def incluirVecino(self, vecino, tiempo=0):
        self.conexiones[vecino] = tiempo
        return


class GrafoVuelos:
    def __init__(self):
        self.aeropuertos = {}
        self.numAeropuertos = 0

    def agregar_aeropuerto(self, nombre):
        nuevoAeropuerto = Aeropuerto(nombre)
        self.aeropuertos[nombre] = nuevoAeropuerto
        self.numAeropuertos += 1
        return nuevoAeropuerto

    def agregar_vuelo(self, origen, destino, tiempo=0):
        if origen not in self.aeropuertos:
            self.agregar_aeropuerto(origen)

        if destino not in self.aeropuertos:
            self.agregar_aeropuerto(destino)

        self.aeropuertos[origen].incluirVecino(destino, tiempo)

        return

    def ruta_mas_corta(self, inicio, destino):
        # Inicialización
        distancias = {a: math.inf for a in self.aeropuertos}
        distancias[inicio] = 0
        predecesores = {}
        no_visitados = set(self.aeropuertos.keys())

        while no_visitados:
            # Aeropuerto no visitado con menor distancia
            actual = min(no_visitados, key=lambda x: distancias[x])
            no_visitados.remove(actual)

            if actual == destino:
                break  # Llegamos al destino

            for vecino, tiempo in self.aeropuertos[actual].conexiones.items():
                nueva_distancia = distancias[actual] + tiempo
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    predecesores[vecino] = actual

        # Reconstruir la ruta
        ruta = []
        actual = destino
        if actual not in predecesores and actual != inicio:
            return None, math.inf  # No hay ruta
        while actual != inicio:
            ruta.insert(0, actual)
            actual = predecesores[actual]
        ruta.insert(0, inicio)

        return ruta, distancias[destino]


red_aerea = GrafoVuelos()
red_aerea.agregar_aeropuerto("Madrid")
red_aerea.agregar_aeropuerto("París")
red_aerea.agregar_aeropuerto("Londres")
red_aerea.agregar_aeropuerto("Munich")
red_aerea.agregar_aeropuerto("Berlín")

red_aerea.agregar_vuelo("Madrid", "París", 120)
red_aerea.agregar_vuelo("Madrid", "Londres", 150)
red_aerea.agregar_vuelo("Madrid", "Munich", 80)
red_aerea.agregar_vuelo("París", "Berlín", 100)
red_aerea.agregar_vuelo("Munich", "Berlín", 70)
red_aerea.agregar_vuelo("Londres", "Berlín", 130)

ruta, tiempo_total = red_aerea.ruta_mas_corta("Madrid", "Berlín")
print(f"Mejor ruta: {ruta} con un tiempo total de {tiempo_total} minutos")
