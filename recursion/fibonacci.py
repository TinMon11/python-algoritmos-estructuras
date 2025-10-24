# La serie de Fibonacci es una secuencia matemática donde cada número es la suma de los dos anteriores, empezando por 0 y 1. La secuencia se ve de la siguiente manera:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# Tu tarea es crear una función recursiva fibonacci(n) que devuelva el n-ésimo número de la secuencia de Fibonacci.
# Requisitos:
# La función fibonacci(n) debe devolver el n-ésimo número de Fibonacci.
# La función debe ser recursiva.
# Implementar un caso base para las condiciones cuando n = 0 o n = 1.
# Ejemplo de uso:
# # Ejemplo de uso:
# print(fibonacci(0))  # Debería devolver 0
# print(fibonacci(1))  # Debería devolver 1
# print(fibonacci(5))  # Debería devolver 5
# print(fibonacci(10))  # Debería devolver 55

def fibonacci(numero):
    if numero == 0:
        return 0
    if numero == 1:
        return 1
    
    return fibonacci(numero -1) + fibonacci(numero-2)

print(fibonacci(0))  # Debería devolver 0
print(fibonacci(1))  # Debería devolver 1
print(fibonacci(5))  # Debería devolver 5
print(fibonacci(10))  # Debería devolver 55



# 5 -> fib(4) + fib(3)
# -> fib(3) + fib(2) + fib(2) + fib(1)
# -> fib(2) + fib(1) + fib(1) + fib(0) + fib(1) + fib(0) + 1
# -> fib(1) + fib(0) + 1 + 1 + 0 + 1 + 0 + 1
# -> 1+ 0 + 1 + 1 + 0 + 1 + 0 + 1