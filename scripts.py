import json
import matplotlib.pyplot as plt
import numpy as np
""" -------------------------------------------------------------------- """
path1 = './datasets/mipymes.json'
path2 = './datasets/salaries.json'
""" -------------------------------------------------------------------- """
def OpenJSON(path):
    # Leer archivos JSON
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data
""" -------------------------------------------------------------------- """
def SAD(day, path=path2):
    # Promedio Diario del Salario
    salaries = OpenJSON(path).get("salaries")
    n_salarie = []

    for i in range(len(salaries)):
        salarie = salaries[i]["salarie"]
        n_salarie.append(salarie)

    return (sum(n_salarie) // len(n_salarie)) // day
""" -------------------------------------------------------------------- """
def AddDicc(k, v1, v2, path=path1, place="place", product="products"):
    # Agrega a un Diccionario claves y valores como: "list()" o "set()"
    mipymes = OpenJSON(path).get("mipymes")
    dicc = {}

    for i in range(len(mipymes)):
        products = mipymes[i][product]
        key = mipymes[i][place][k]
        
        if key not in dicc:
            dicc[key] = v1
        
        for j in range(len(products)):
            value = products[j][v2]
            dicc[key].add(value)

    return dicc
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """
def Origin(n, path=path1):
    mipymes = OpenJSON(path).get("mipymes")
    counter = {}

    for i in range(len(mipymes)):
        products = mipymes[i]["products"]

        for j in range(len(products)):
            origin = products[j]["origin"]

            if (origin != "") and (origin != None):
                if origin in counter:
                    counter[origin] += 1
                else:
                    counter[origin] = 1

    for _ in range(n):
        max_key = None
        max_value = -1

        for k, v in counter.items():
            if v > max_value:
                max_value = v
                max_key = k

        print(f'{max_key}: {max_value}')
        del counter[max_key]
""" -------------------------------------------------------------------- """