import json
""" -------------------------------------------------------------------- """
path1 = './datasets/mipymes.json'
path2 = './datasets/salaries.json'
""" -------------------------------------------------------------------- """
def OpenJSON(path):
    # Leer archivos en formato JSON
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data
""" -------------------------------------------------------------------- """
def Dicc(k, v, path=path1):
    # Agrega a un diccionario claves["Place"] y valores["Products"]
    # Valores: Categorías o subcategorías sín repetir
    mipymes = OpenJSON(path).get("mipymes")
    dicc = {}

    for i in range(len(mipymes)):
        products = mipymes[i]["products"]
        key = mipymes[i]["place"][k]
        
        if key not in dicc:
            dicc[key] = set()
        
        for j in range(len(products)):
            value = products[j][v]
            dicc[key].add(value)

    return dicc.items()
""" -------------------------------------------------------------------- """
def Dicc2(k, v, path=path1):
    # Agrega a un diccionario claves["Products"] y valores["Products"]
    # Valores: Lista de cantidades de peso neto
    mipymes = OpenJSON(path).get("mipymes")
    dicc = {}

    for i in range(len(mipymes)):
        products = mipymes[i].get("products")

        for j in range(len(products)):
            key = products[j][k]
            value = products[j][v]

            if value is None:
                continue
            if key not in dicc:
                dicc[key] = []
            dicc[key].append(value)

    return dicc.items()
""" -------------------------------------------------------------------- """
def Dicc3(k, path=path1):
    # Agrega a un diccionario
    mipymes = OpenJSON(path).get("mipymes")
    dicc = {}

    for i in range(len(mipymes)):
        products = mipymes[i]["products"]

        for j in range(len(products)):
            key = products[j][k]

            if key == "" or key is None:
                continue
            dicc[key] = dicc.get(key, 0) + 1

    return dicc
""" -------------------------------------------------------------------- """
def OrderDicc(k, n):
    # Ordena el diccionario por valores (enteros)
    items = [i for i in Dicc3(k).items()]
    for i in range(len(items)):
        min = i
        for j in range(i+1, len(items)):
            if items[j][1] > items[min][1]:
                min = j
        items[i], items[min] = items[min], items[i]

    dicc = {k:v for k,v in items[:n]}
    return dicc
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """