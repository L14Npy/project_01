import json
import matplotlib.pyplot as plt
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
            dicc[key] = set()
        
        for j in range(len(products)):
            value = products[j][v2]
            dicc[key].add(value)

    return dicc.items()
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """