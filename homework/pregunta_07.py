"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 2 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]
    """
    # Abrimos y leemos el archivo
    with open("./files/input/data.csv", "r") as file:
        data = file.readlines()

    # Crear un diccionario para asociar los valores de la columna 2 con las letras de la columna 1
    col2_dict = {}

    # Procesar cada línea
    for line in data:
        # Separar las columnas
        columns = line.strip().split("\t")
        letter = columns[0]  # Columna 1 (letra)
        col2_value = int(columns[1])  # Columna 2 (valor numérico)

        # Asociar la letra al valor de la columna 2 en el diccionario
        if col2_value not in col2_dict:
            col2_dict[col2_value] = [letter]
        else:
            col2_dict[col2_value].append(letter)

    # Ordenar el diccionario por las claves (valores de la columna 2)
    result = sorted(col2_dict.items())

    return result

# Llamar a la función y probar
print(pregunta_07())

