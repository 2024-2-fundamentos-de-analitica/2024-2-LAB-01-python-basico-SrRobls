"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    with open('./files/input/data.csv', mode='r', encoding='utf-8') as f:
        data = f.readlines()
        maximo_minimo = [line.split()[0:2] for line in data]
        # print(maximo_minimo)

        dict_results = {}

        # for line in data:
        for letra, value in maximo_minimo:
            value = int(value)
            # print(list(dict_results.keys()))
            if letra in list(dict_results.keys()):
                # print(dict_results[letra])
                if dict_results[letra][0] < value:
                    dict_results[letra][0] = value
                if dict_results[letra][1] > value:
                    dict_results[letra][1] = value
            else:
                dict_results[letra[0]] = [value, value]
    
        return sorted(tuple((r[0], r[1][0], r[1][1]))for r in dict_results.items())
    
print(pregunta_05())

    
