# Dada una cadena `s` que contiene únicamente los caracteres `'('`, `')'`, `'{'`, `'}'`, `'['` y `']'`, determina si la cadena es válida.

# Una cadena es válida si se cumplen las siguientes condiciones:
# 1. Los paréntesis abiertos deben cerrarse con el mismo tipo de paréntesis.
# 2. Los paréntesis abiertos deben cerrarse en el orden correcto.
# 3. Todo paréntesis de cierre debe tener un paréntesis de apertura correspondiente del mismo tipo.

# **Ejemplo 1**
# Entrada: `s = "()"`
# Salida: `true`
# Explicación: El paréntesis se abre y se cierra correctamente con el mismo tipo y en el orden adecuado.

# **Ejemplo 2**
# Entrada: `s = "{[()]}"`
# Salida: `true`
# Explicación: Todos los paréntesis se abren y cierran en el orden correcto y con el tipo correspondiente: `{ → [, ( → ), ] → }`.

# **Ejemplo 3 (inválido)**
# Entrada: `s = "(]"`
# Salida: `false`
# Explicación: El paréntesis redondo se abre pero se intenta cerrar con corchete, lo cual es incorrecto.

# **Ejemplo 4 (inválido)**
# Entrada: `s = "([)]"`
# Salida: `false`
# Explicación: Aunque los tipos coinciden, el orden es incorrecto: el paréntesis redondo se cierra antes que el corchete que lo contiene.


def balanceado(cadena):

    # cerrador - abridor
    mapping = {"}": "{", "]": "[", ")": "("}
    stack = []

    if len(cadena) % 2 != 0:
        return False

    for letra in cadena:
        # Si letra es cerrador, el ultimo elemento del stack deberia ser el abridor correspondiente a ese cerrador
        if letra in mapping.keys():
            if len(stack) == 0:
                return False
            # Vemos si el ultimo del stack es el abridor correspondiente
            if mapping[letra] != stack.pop():
                # Eran distintos, retorno False
                return False
        else:
            # Es un abridor, lo agregamos al stack
            stack.append(letra)

    return True


def run_tests():
    assert (balanceado('[[[[[[[()]]]]]]]')) == True
    assert (balanceado('[[[[[[[()]]]]')) == False
    assert (balanceado('{}()[[]')) == False
    
    return "- Test successfull"

print(run_tests())