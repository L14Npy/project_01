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

    return sorted(dicc.values())
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """
def NI(made, path=path1):
    # Genera una Gráfica de Tipo Pastel de Porcentajes de Productos "Nacionales VS Internacionales"
    made = made.upper()
    mipymes = OpenJSON(path).get("mipymes")
    n_national = []
    n_international = []

    for i in range(len(mipymes)):
        products = mipymes[i].get("products")

        for j in range(len(products)):
            origin = products[j]["origin"]

            if (origin is None) or (origin == ''):
                continue
            if origin == made:
                n_national.append(origin)
            else:
                n_international.append(origin)

    labels = [f'{made}', 'Internacionales']
    sizes = [len(n_national), len(n_international)]

    plt.figure(figsize=(6,6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title(f"Distribución de Productos: {made} vs Internacionales")
    plt.show()
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """
def Origin(n, path=path1):
    # Genera una Gráfica de Tipo Pastel de Porcentajes de Productos de su País de Procedencia
    mipymes = OpenJSON(path).get("mipymes")
    counter = {}

    for i in range(len(mipymes)):
        products = mipymes[i]["products"]

        for j in range(len(products)):
            origin = products[j]["origin"]

            if origin == "" or origin is None:
                continue
            counter[origin] = counter.get(origin, 0) + 1

    dicc = {}
    for _ in range(n):
        if not counter:
            break

        max_key = None
        max_value = -1

        for k, v in counter.items():
            if v > max_value:
                max_value = v
                max_key = k
        dicc[max_key] = max_value
        del counter[max_key]

    labels = [i for i in dicc.keys()]
    values = [j for j in dicc.values()]

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.title(f"Top {n} Orígenes de Productos")
    plt.axis("equal")
    plt.show()

    return dicc
""" -------------------------------------------------------------------- """
def Origin2(n, path=path1):
    # Genera una Gráfica de Tipo Pastel de Porcentajes de Productos de su País de Procedencia
    mipymes = OpenJSON(path).get("mipymes")
    counter = {}

    for i in range(len(mipymes)):
        products = mipymes[i]["products"]

        for j in range(len(products)):
            origin = products[j]["origin"]

            if origin == "" or origin is None:
                continue
            counter[origin] = counter.get(origin, 0) + 1

    dicc = {}
    for _ in range(n):
        if not counter:
            break

        max_key = None
        max_value = -1

        for k, v in counter.items():
            if v > max_value:
                max_value = v
                max_key = k
        dicc[max_key] = max_value
        del counter[max_key]

    labels = [i for i in dicc.keys()]
    values = [j for j in dicc.values()]

    plt.figure(figsize=(10,6))
    plt.barh(labels, values)
    plt.title(f'Top {n} Orígenes de Productos')
    plt.xlabel('Cantidad')
    plt.ylabel('País')
    plt.yticks(rotation=45, ha='right')
    plt.grid(axis='x', linestyle='--', alpha=0.4)
    plt.show()
""" -------------------------------------------------------------------- """