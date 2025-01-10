"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    with open('./files/input/data.csv', mode='r', encoding='utf-8') as f:
        data = f.readlines() # Leer todas las lineas del archivo

        # Iteramos las filas del archivo y sumamos la segunda columna

        suma = sum([int(filas.split()[1]) for filas in data])

        return suma



# print(pregunta_01())
