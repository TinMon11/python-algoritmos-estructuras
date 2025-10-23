# Imagina que estamos desarrollando una aplicación para gestionar las tareas de un equipo de trabajo. Cada tarea tiene un nombre, una descripción, una fecha de vencimiento y una prioridad. Queremos realizar varias operaciones con las tareas, como:
# Agregar una nueva tarea.
# Eliminar una tarea.
# Actualizar una tarea (por ejemplo, cambiar la prioridad o la fecha de vencimiento).
# Mostrar todas las tareas ordenadas por prioridad.

# Enunciado:
# Crea un programa en Python que permita gestionar un registro de tareas utilizando listas de diccionarios. Cada tarea debe estar representada por un diccionario con los campos: nombre, descripcion, fecha_vencimiento y prioridad. Las operaciones que se deben realizar son las siguientes:

# Agregar ta|rea: Añadir una nueva tarea al registro.

# Eliminar tarea: Eliminar una tarea del registro.

# Actualizar tarea: Modificar la prioridad o la fecha de vencimiento de una tarea.

# Mostrar tareas: Mostrar todas las tareas ordenadas por prioridad (de mayor a menor).

tarea_1 = {
    "nombre": "limpiar",
    "descripcion": "limpiar la cocina",
    "fecha_vencimiento": "12/10/1990",
    "prioridad": "high",
}
tarea_2 = {
    "nombre": "cocinar",
    "descripcion": "cocinar verduras",
    "fecha_vencimiento": "25/12/2026",
    "prioridad": "low",
}
tarea_3 = {
    "nombre": "comprar",
    "descripcion": "comprar carne",
    "fecha_vencimiento": "11/10/2025",
    "prioridad": "high",
}

tareas = [tarea_1, tarea_2, tarea_3]


class TareasManager:
    def add_task(self, tareas, name, description, date, priority):
        tareas.append(
            {
                "nombre": name,
                "descripcion": description,
                "fecha_vencimiento": date,
                "prioridad": priority,
            }
        )

    def delete_task(self, tareas, name):
        for index, tarea in enumerate(tareas):
            if tarea["nombre"] == name:
                del tareas[index]
                return

    def modify_task(self, tareas, name, priority, date):
        for index, tarea in enumerate(tareas):
            if tarea["nombre"] == name:
                if priority:
                    tarea["prioridad"] = priority
                if date:
                    tarea["fecha_vencimiento"] = date

                return


manager = TareasManager()

print(tareas)

manager.add_task(tareas, "pintar", "Pintar la casa", "22/10/1555", "low")

manager.delete_task(tareas, "cocinar")

print(tareas)

manager.modify_task(tareas, "limpiar", "low", "01/01/2020")
print(tareas)
