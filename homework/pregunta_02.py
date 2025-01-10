"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    with open('./files/input/data.csv', mode='r', encoding='utf-8') as f:
        data = f.readlines()

        letras = [str(fila.split()[0]) for fila in data]
        set_letras = sorted(set(letras))

        conteo = [(letra, letras.count(letra)) for letra in set_letras]


        return conteo
    


# print(pregunta_02())


