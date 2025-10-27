# Dada una lista, devolver otra donde cada elemento sea la mutliplicacion de los otros elementos de la primer lista
# [1,4,5,6] -> [120, 30, 24, 20]

def multiplica(lista):
    respuesta = [None] * len(lista)
    
    for i, numero in enumerate(lista):
        mult = 1
        for indice2, numero2 in enumerate(lista):
            if i != indice2:
                mult = mult * numero2
        respuesta[i] = mult
        
    return respuesta

print("Multiplicado ...", multiplica([1,4,5,6]))