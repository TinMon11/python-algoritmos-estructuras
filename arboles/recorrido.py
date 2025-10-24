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

    def insertar_izquierda(self, valor):
        if self.izquierdo is None:
            self.izquierdo = ArbolBinario(valor)
        else:
            arbol = ArbolBinario(valor)
            arbol.izquierdo = self.izquierdo
            self.izquierdo = arbol

    def insertar_derecha(self, valor):
        if self.derecho is None:
            self.derecho = ArbolBinario(valor)
        else:
            arbol = ArbolBinario(valor)
            arbol.derecho = self.derecho
            self.derecho = arbol

    def getRaiz(self):
        return self.raiz

    def getIzquierdo(self):
        return self.izquierdo

    def getDerecho(self):
        return self.derecho

    def setRaiz(self, nuevoValor):
        self.raiz.valor = nuevoValor


def preorder(arbol: ArbolBinario):
    if arbol:
        print(arbol.getRaiz().valor)
        preorder(arbol.getIzquierdo())
        preorder(arbol.getDerecho())


def preorder(arbol: ArbolBinario):
    if arbol:
        print(arbol.getRaiz().valor)
        preorder(arbol.getIzquierdo())
        preorder(arbol.getDerecho())
    # else:
    #     print("--")
    
def mostrar_arbol_horizontal(nodo, nivel=0):
    if nodo is not None:
        mostrar_arbol_horizontal(nodo.derecho, nivel + 1)
        print("    " * nivel + str(nodo.getRaiz().valor))
        mostrar_arbol_horizontal(nodo.izquierdo, nivel + 1)



# Crear árbol con raíz A
arbol = ArbolBinario("A")
arbol.insertar_izquierda("B")
arbol.insertar_derecha("C")
# arbol.insertar_derecha("D")
# arbol.insertar_izquierda("F")
# arbol.insertar_izquierda("G")

# preorder(arbol)

mostrar_arbol_horizontal(arbol)