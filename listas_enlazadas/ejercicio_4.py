# Historial de navegacion web con lista doblemente enalzada que permita ir hacia adlenta y atras (no circular)


# Clase Nodo
class Nodo:
    def __init__(self, url):
        self.url = url
        self.anterior = None
        self.siguiente = None


# Clase Historial de Navegación
class HistorialNavegacion:
    def __init__(self):
        self.actual = None  # nodo actual (donde está el usuario)
        self.cabeza = None  # inicio del historial

    def agregar_pagina(self, url):
        nuevo = Nodo(url)
        if self.cabeza is None:
            # si la lista está vacía
            self.cabeza = nuevo
            self.actual = nuevo
        else:
            # si estamos en medio del historial y agregamos una nueva página,
            # se pierde lo que estaba "adelante"
            self._borrar_hacia_adelante()

            # agregamos la nueva página al final
            self.actual.siguiente = nuevo
            nuevo.anterior = self.actual
            self.actual = nuevo

    def _borrar_hacia_adelante(self):
        """Elimina los nodos hacia adelante desde la página actual."""
        if self.actual and self.actual.siguiente:
            self.actual.siguiente = None

    def retroceder(self):
        if self.actual is None or self.actual.anterior is None:
            return "No hay más páginas anteriores."
        self.actual = self.actual.anterior
        return self.actual.url

    def avanzar(self):
        if self.actual is None or self.actual.siguiente is None:
            return "No hay más páginas hacia adelante."
        self.actual = self.actual.siguiente
        return self.actual.url

    def mostrar_historial(self):
        paginas = []
        actual = self.cabeza
        while actual:
            paginas.append(actual.url)
            actual = actual.siguiente
        return " -> ".join(paginas) if paginas else "Historial vacío."

    def pagina_actual(self):
        if self.actual:
            return self.actual.url
        return "No hay página actual."


# ---------------------------
# Ejemplo de uso
# ---------------------------

historial = HistorialNavegacion()

# Agregar páginas al historial
historial.agregar_pagina("pagina1.com")
historial.agregar_pagina("pagina2.com")
historial.agregar_pagina("pagina3.com")

print("Historial de navegación:")
print(historial.mostrar_historial())  # pagina1.com -> pagina2.com -> pagina3.com

# Retroceder
print("\nRetrocediendo...")
print(historial.retroceder())  # pagina2.com
print(historial.retroceder())  # pagina1.com
print(historial.retroceder())  # No hay más páginas anteriores.

# Avanzar
print("\nAvanzando...")
print(historial.avanzar())  # pagina2.com
print(historial.avanzar())  # pagina3.com
print(historial.avanzar())  # No hay más páginas hacia adelante.

# Página actual
print("\nPágina actual:", historial.pagina_actual())  # pagina3.com
print(historial.retroceder()) 
print("\nPágina actual si retrocedo de nuevo:", historial.pagina_actual())  # pagina3.com
