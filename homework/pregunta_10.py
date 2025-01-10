"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas que contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]
    """
    # Abrimos y leemos el archivo
    with open("./files/input/data.csv", "r") as file:
        data = file.readlines()

    # Crear una lista para almacenar el resultado
    result = []

    # Procesar cada línea
    for line in data:
        # Separar las columnas
        columns = line.strip().split("\t")
        letter = columns[0]  # Columna 1 (letra)
        col4_elements = len(columns[3].split(","))  # Cantidad de elementos en la columna 4
        col5_elements = len(columns[4].split(","))  # Cantidad de elementos en la columna 5

        # Añadir la tupla (letra, elementos en col 4, elementos en col 5) al resultado
        result.append((letter, col4_elements, col5_elements))

    return result

# Llamar a la función y probar
print(pregunta_10())

