import json
""" ----------------------------------------- """
def OpenJSON(path:str):
    """
    Lector de archivos JSON
    """
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data
""" ----------------------------------------- """
pymes = OpenJSON('./data/mipymes.json')
exchanges = OpenJSON('./data/exchanges.json')
salaries = OpenJSON('./data/salaries.json')
basket = OpenJSON('./data/basket.json')
""" ----------------------------------------- """
def DataCount(data:dict) -> int:
    """
    Contador de elementos
    """
    counter = 0
    for i in data:
        counter += 1
    return counter
""" ----------------------------------------- """
data_count = DataCount(pymes)
""" ----------------------------------------- """
def GetProducts() -> dict:
    """
    Extrae un diccionario los nombres (MiPymes) y productos
    """
    dicc = {}
    for i in pymes:
        for j in i.get('products', []):
            if i['name'] not in dicc:
                dicc[i['name']] = set()
            dicc[i['name']].add(j['category'])
    return dicc
""" ----------------------------------------- """
def CountProducts() -> dict:
    """
    Extrae en un diccionario las cantidad de productos
    por categoría
    """
    dicc = {}
    for i in pymes:
        for j in i.get('products', []):
            category = j['category']
            dicc[category] = dicc.get(category, 0) + 1
    return dicc
""" ----------------------------------------- """
def CountProducts2() -> dict:
    """
    Extrae en un diccionario las cantidad de productos
    por MiPyme
    """
    dicc = {}
    for i in pymes:
        name = i['name']
        for j in i.get('products', []):
            category = j['category']
            if name not in dicc:
                dicc[name] = []
            dicc[name].append(category)

    dicc2 = {}
    for k,v in dicc.items():
        dicc2[k] = len(v)
    return dicc2
""" ----------------------------------------- """
def CountOrigin() -> dict:
    """
    Extrae un diccionario que cuenta la cantidad
    de productos por su procedencia
    """
    dicc = {}
    for i in pymes:
        for j in i.get('products', []):
            origin = j['origin']
            if origin is None:
                continue
            dicc[origin] = dicc.get(origin, 0) + 1
    return dicc
""" ----------------------------------------- """
def AveragePyme() -> dict:
    """
    Extrae en un diccionario el nombre (MiPyme) y su precio promedio
    """
    dicc = {}
    for i in pymes:
        name = i['name']
        dicc[name] = []
        for j in i.get('products', []):
            for k in j.get('records', []):
                price = k['price']
            dicc[name].append(price)

    average = {}
    for k,v in dicc.items():
        average[k] = sum(v) // len(v)
    return average
""" ----------------------------------------- """
def AverageProducts() -> dict:
    """
    Extrae en un diccionario el precio promedio
    de los productos
    """
    dicc = {}
    for i in pymes:
        for j in i.get('products', []):
            category = j['category']
            if category == 'huevos':
                continue
            if category not in dicc:
                dicc[category] = []
            for k in j.get('records', []):
                price = k['price']
                dicc[category].append(price)

    average = {}
    for k,v in dicc.items():
        average[k] = sum(v) // len(v)
    return average
""" ----------------------------------------- """
def AverageSalarie(day) -> int:
    """
    Retorna el salario promedio
    """
    sum = 0
    count = 0
    for i in salaries:
        sum += i['salary']
        count += 1
    return (sum // count) // day
""" ----------------------------------------- """
def UnitaryProducts() -> dict:
    """
    Extrae en un diccionario una lista de gramaje
    por producto
    """
    dicc = {}
    for i in pymes:
        for j in i.get('products', []):
            category = j['category']
            count = j['count']
            if category not in dicc:
                dicc[category] = []
            dicc[category].append(count)
    return dicc
""" ----------------------------------------- """
def PriceProducts() -> dict:
    """
    Extrae en un diccionario la lista de precios de
    cada producto
    """
    dicc = {}
    for i in pymes:
        for j in i.get('products', []):
            category = j['category']
            if category not in dicc:
                dicc[category] = []
            for k in j.get('records', []):
                price = k['price']
                dicc[category].append(price)
    return dicc
""" ----------------------------------------- """
def CostBasket() -> float:
    """
    Retorna el costo promedio de la canasta
    """
    cost = 0
    for k,v in basket.items():
        if k == 'huevos':
            continue
        if k in AverageProducts():
            cost += AverageProducts()[k] * v
    return round(cost,0)
""" ----------------------------------------- """
def CostBasket2() -> dict:
    """
    Extrae en un diccionario el costo promedio
    de los productos por su gramaje
    """
    dicc = {}
    for k,v in basket.items():
        if k == 'huevos':
            continue
        if k in AverageProducts():
            dicc[k] = AverageProducts()[k] * v
    return dicc
""" ----------------------------------------- """
def ListProducts() -> dict:
    """
    Extrae en un diccionario la lista de precios
    de los productos
    """
    dicc = {}
    for i in pymes:
        for j in i.get('products', []):
            category = j['category']
            if category == 'huevos':
                continue
            if category not in dicc:
                dicc[category] = []
            for k in j.get('records', []):
                price = k['price']
                dicc[category].append(price)
    return dicc
""" ----------------------------------------- """
def PercentSalary() -> dict:
    """
    Extrae en un diccionario el porcentaje del salario necesario
    para comprar cada producto
    """
    dicc = {}
    for k,v in CostBasket2().items():
        dicc[k] = round((v / AverageSalarie(1)) * 100, 0)
    return dicc
""" ----------------------------------------- """
def NecesaryDays(day):
    """
    Extrae en un diccionario los días necesarios
    para adquirir un producto
    """
    dicc = {}
    for k,v in CostBasket2().items():
        dicc[k] = v // AverageSalarie(day)
    return dicc
""" ----------------------------------------- """
""" ----------------------------------------- """
""" ----------------------------------------- """