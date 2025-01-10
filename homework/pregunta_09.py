"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    with open('./files/input/data.csv', mode='r') as f:
        data = f.readlines()

    result = {}

    columna = [line.strip().split()[4].split(',') for line in data]

    for c in columna:
        for i in c:
            i = i.split(':')
            key = i[0]
            value = i[1]
            if not key in result:
                result[key] = 1
            else:
                result[key] += 1

    result = dict(sorted(result.items()))
    return result

print(pregunta_09())

