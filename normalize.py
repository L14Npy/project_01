import json
""" ------------------------------------------------------------- """
def OpenJSON(path, k):
    # Abre documentos en formato JSON
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get(k, [])
""" ------------------------------------------------------------- """
mipymes = OpenJSON('./datasets/mipymes.json', 'mipymes')
salaries = OpenJSON('./datasets/salaries.json', 'salaries')
""" ------------------------------------------------------------- """
def Sum(array):
    # Retorna la suma de una lista
    sum = 0
    for i in array:
        sum += i
    return sum
""" ------------------------------------------------------------- """
def Average():
    # Retorna el promedio total de una lista
    array = []
    for i in salaries:
        array.append(i["salarie"])
    return Sum(array) // len(array)
""" ------------------------------------------------------------- """
average = Average()
""" ------------------------------------------------------------- """
def DiccJSON(k):
    # Genera un diccionario con claves específicas a partir del archivo JSON
    dicc = {}
    for i in mipymes:
        for j in i["products"]:
            key = j[k]
            if key not in dicc:
                dicc[key] = []
            dicc[key].append(j["count"])
    return dicc
""" ------------------------------------------------------------- """
def Dicc(k):
    # Genera un diccionario con el valor moda
    dicc = {}
    for k,v in DiccJSON(k).items():
        val = Moda(v)
        dicc[k] = val
    return dicc
""" ------------------------------------------------------------- """
def DiccOrder(k, rg):
    # Organiza el diccionario en orden alfabético
    array = [i for i in Dicc(k).items()]
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[j][0] < array[min][0]:
                min = j
        array[i], array[min] = array[min], array[i]
    return {k:v for k,v in array[:rg]}
""" ------------------------------------------------------------- """
def DiccOrder2(f, k, rg):
    # Organiza el diccionario en orden numérico
    array = [i for i in f(k).items()]
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[j][1] > array[min][1]:
                min = j
        array[i], array[min] = array[min], array[i]
    return {k:v for k,v in array[:rg]}
""" ------------------------------------------------------------- """
def DiccOrder3(f, k, rg):
    # Organiza el diccionario en orden numérico
    array = [i for i in f(k).items()]
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[j][1] < array[min][1]:
                min = j
        array[i], array[min] = array[min], array[i]
    return {k:v for k,v in array[:rg]}
""" ------------------------------------------------------------- """
def DiccCounter(k):
    dicc = {}
    for i in mipymes:
        for j in i.get("products", []):
            key = j.get(k, None)
            if key is None:
                continue
            if key is not None:
                dicc[key] = dicc.get(key, 0) + 1
    return dicc
""" ------------------------------------------------------------- """
def DiccCounter2(k, v1, v2='CU'):
    v1 = v1.upper()
    dicc = {}
    for i in mipymes:
        for j in i.get("products", []):
            key = j.get(k, None)
            if key is None:
                continue
            if key not in (v1, v2):
                continue
            dicc[key] = dicc.get(key, 0) + 1
    return dicc
""" ------------------------------------------------------------- """
def Moda(array):
    # Retorna el elemento que más se repite
    repeat = 0
    moda = None
    for i in range(len(array)):
        counter = 0
        for j in range(len(array)):
            if array[j] == array[i]:
                counter += 1
        if counter > repeat:
            repeat = counter
            moda = array[i]
    return moda
""" ------------------------------------------------------------- """
def DoubleList(k):
    nationals = []
    internationals = []
    for i in mipymes:
        for j in i.get("products", []):
            key = j.get(k)
            if key == 'CU':
                nationals.append(key)
            else:
                internationals.append(key)
    return len(nationals), len(internationals)
""" ------------------------------------------------------------- """
""" ------------------------------------------------------------- """
""" ------------------------------------------------------------- """
""" ------------------------------------------------------------- """