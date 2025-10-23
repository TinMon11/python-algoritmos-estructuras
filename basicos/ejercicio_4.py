# Imaginemos que tenemos un sistema para registrar estudiantes y sus calificaciones en distintas asignaturas. Queremos realizar las siguientes tareas utilizando las estructuras de datos básicas:
# Diccionario de estudiantes: Crear un diccionario que asocie a cada estudiante con un conjunto de calificaciones (cada estudiante puede tener varias calificaciones para diferentes asignaturas).
# Promedio de calificaciones: Crear una función que calcule el promedio de calificaciones de cada estudiante.
# Estudiantes aprobados: Crear una lista con los nombres de los estudiantes que tienen un promedio mayor o igual a 6 (nota de aprobación).
# Estudiantes únicos: Crear un conjunto con los nombres únicos de los estudiantes (es posible que se repitan en el registro).

# Enunciado:
# Crea una función llamada procesar_estudiantes que reciba un diccionario con los nombres de los estudiantes como claves y una lista de sus calificaciones como valores. La función debe devolver:
# Un diccionario con los nombres de los estudiantes como claves y sus promedios de calificaciones como valores redondeados a 2 decimales.
# Una lista con los nombres de los estudiantes que tienen un promedio de calificación mayor o igual a 6.
# Un conjunto con los nombres únicos de los estudiantes (en caso de que haya estudiantes repetidos).

# Ejemplo

# Entrada:
# estudiantes = {
#     'Juan': [8, 7, 9],
#     'Ana': [5, 6, 4],
#     'Carlos': [10, 9, 9],
#     'Luis': [4, 3, 5],
#     'Ana': [6, 7, 6]  # Ana se repite en el registro con diferentes calificaciones
# }
# Ejecutar función e imprimir resultados:
# resultado = procesar_estudiantes(estudiantes)
# print(resultado)
# Salida esperada:

# ({'Juan': 8.0, 'Ana': 6.333333333333333, 'Carlos': 9.333333333333334, 'Luis': 4.0}, ['Juan', 'Ana', 'Carlos'], {'Ana', 'Luis', 'Carlos', 'Juan'})

estudiantes = {
    "Juan": [8, 7, 9],
    "Ana": [5, 6, 4],
    "Carlos": [10, 9, 9],
    "Luis": [4, 3, 5],
    "Ana": [6, 7, 6],  # Ana se repite en el registro con diferentes calificaciones
}


def procesar_estudiantes(estudiantes):

    resultado = []
    promedios = {}
    aprobados = []
    lista_unica = []

    for estudiante in estudiantes:
        notas = estudiantes[estudiante]
        promedio = sum(notas) / len(notas)
        promedios[estudiante] = round(max(promedios.get(estudiante, 0), promedio), 2)
        if promedio > 6:
            aprobados.append(estudiante)

    lista_unica = set(estudiantes)

    resultado.append(promedios)
    resultado.append(aprobados)
    resultado.append(lista_unica)
    
    return resultado


print(procesar_estudiantes(estudiantes))
