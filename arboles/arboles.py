# Hay un nodo principal del que cuelgan otros nodos
# Como si fueran las ramas de un arbol
# "hojas" son las ultimso nodos, cuando no tienen ramas
# Cada nodo puede no tener hijos, o tener mas 1 o mas hijos
# Si cada nodo tiene dos hijos, es un arbol binario

# Se crea basciamente con listas enalzadas que contienen listas enlazadas


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinario:
    def __init__(self, raiz_valor):
        self.raiz = Nodo(raiz_valor)
        self.izquierdo = None
        self.derecho = None

    def insertar_izquierda(self, Nodo):
        """Inserta un nodo a la izquierda de 'nodo'.
        Si ya existe un hijo izquierdo, se convierte en hijo del nuevo nodo."""
        if self.izquierdo == None:
            self.izquierdo = ArbolBinario(Nodo)
        else:
            arbol = ArbolBinario(Nodo)
            arbol.izquierdo = self.izquierdo
            self.izquierdo = arbol

    def insertar_derecha(self, Nodo):
        """Inserta un nodo a la izquierda de 'nodo'.
        Si ya existe un hijo izquierdo, se convierte en hijo del nuevo nodo."""
        if self.derecho == None:
            self.derecho = ArbolBinario(Nodo)
        else:
            arbol = ArbolBinario(Nodo)
            arbol.derecho = self.derecho
            self.derecho = arbol

    def getRaiz(self):
        """Muestra el árbol de manera jerárquica"""
        return self.raiz

    def getIzquierdo(self):
        return self.izquierdo

    def getDerecho(self):
        return self.derecho

    def setRaiz(self, nuevoValor):
        self.valor = nuevoValor


# Crear árbol con raíz A
arbol = ArbolBinario("A")

arbol.insertar_izquierda("B")
arbol.insertar_derecha("C")
arbol.insertar_derecha("C")

print(arbol.getRaiz())

