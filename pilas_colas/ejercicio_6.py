# Descripción:
# Imagina que trabajas en un banco y debes desarrollar un sistema para gestionar la fila de clientes que esperan ser atendidos. Cada cliente tiene un número de turno y es atendido en el orden en que llegó (FIFO - First In, First Out).
# Objetivo:
# Implementar una estructura de datos que simule una cola de atención al cliente, permitiendo agregar clientes a la fila y atenderlos en el orden correcto.
# Instrucciones:
# 1️⃣ Crea una clase ColaBanco con los siguientes métodos:
# llegar_cliente(nombre: str): Agrega un nuevo cliente a la cola con un número de turno.
# atender_cliente(): Atiende al cliente que llegó primero y lo elimina de la cola.
# mostrar_cola(): Devuelve una lista con los clientes en espera.

# 2️⃣ Usa una cola (FIFO) para almacenar los clientes en el orden en que llegaron.
# 3️⃣ Cada cliente debe tener un número de turno único que se incrementa automáticamente.
# 4️⃣ Simula la llegada y atención de clientes con diferentes operaciones.


class ColaBanco:
    def __init__(self):
        self.clientes = []
        self.turno = 0

    def llegar_clientes(self, nombre):
        self.turno += 1
        return self.clientes.append({"nombre": nombre, "turno": self.turno})

    def atender_cliente(self):
        if self.clientes:
            return self.clientes.pop(0)
        else:
            return

    def mostrar_cola(self):
        return self.clientes


cola_banco = ColaBanco()

cola_banco.llegar_clientes("Juan")
cola_banco.llegar_clientes("Martin")
cola_banco.llegar_clientes("Pedro")
print("Cola:", cola_banco.mostrar_cola())
cola_banco.atender_cliente()
cola_banco.atender_cliente()
print("Cola:", cola_banco.mostrar_cola())

cola_banco.llegar_clientes("Susana")
cola_banco.llegar_clientes("Susanita")
cola_banco.atender_cliente()
print("Cola:", cola_banco.mostrar_cola())
