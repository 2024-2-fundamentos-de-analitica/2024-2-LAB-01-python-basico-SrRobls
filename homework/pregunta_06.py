"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    with open('./files/input/data.csv', mode='r') as f:
        data = f.readlines()


        lineas = [line.split()[4].split(',') for line in data]

        result = {}

        for line in lineas:
            for item in line:
                item = item.split(':')
                # print(item)
                clave = item[0]
                value = int(item[1])
                if not clave in result:
                    result[clave] = [value, value]
                else:
                    result[clave][0] = min(result[clave][0], value)
                    result[clave][1] = max(result[clave][1], value)
            



        return sorted((r[0], r[1][0], r[1][1]) for r in result.items())


print(pregunta_06())
