import json
import numpy as np
import matplotlib.pyplot as plt
""" ------------------------------------------------------ """
def OpenJSON(path:str):
    """
    Abrir archivos de formato JSON
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

pymes = OpenJSON('./data/pymes.json')
salaries = OpenJSON('./data/salaries.json')
exchanges = OpenJSON('./data/exchanges.json')
""" ------------------------------------------------------ """
def Moda(array:list):
    """
    Retorna el elemento más repetido  
    """
    repeat = 0
    moda = None
    for i in range(len(array)):
        counter = 0
        for j in range(len(array)):
            if array[i] == array[j]:
                counter += 1
        if counter > repeat:
            repeat = counter
            moda = array[i]
    return moda
""" ------------------------------------------------------ """
def AverageList(array:list):
    """ Retorna el promedio de una lista """
    return sum(array) // len(array)
""" ------------------------------------------------------ """
def AverageSalarie(day) -> int:
    """
    Retorna el salario promedio/día
    """
    sum = 0
    count = 0
    for i in salaries:
        sum += i['salary']
        count += 1
    return (sum // count) // day
""" ------------------------------------------------------ """
def MaxUnits(day:int):
    """
    Máximo de compra por unidades 
    """
    dicc = {}
    for k, v in basket.items():
        price = v['last']['price']
        dicc[k] = AverageSalarie(day) / price

    return dicc
""" ------------------------------------------------------ """
def NecesaryDays(day:int):
    """
    Días necesarios para adquirir un producto  
    """
    dicc = {}
    for k, v in basket.items():
        price = v['last']['price']
        dicc[k] = price / AverageSalarie(day)

    return dicc
""" ------------------------------------------------------ """
def Basket():
    """
    Genera una estructura JSON con datos de la canasta básica  
    """
    dicc = {}
    for i in pymes:
        for j in i.get('products', []):
            category = j.get('category')
            subcategory = j.get('subcategory')
            unit = j.get('unit')
            count = j.get('count')
            brand = j.get('brand')
            origin = j.get('origin')

            if category == 'leche' and unit == 'kg':
                continue
            if subcategory == 'cartón':
                continue
            if origin == '':
                continue
            if category not in dicc:
                dicc[category] = {
                    'counts': 0,
                    'unit': unit,
                    'weight': [],
                    'made': {
                        'brands': [],
                        'origins': set()
                    },
                    'range': {
                        'min': [],
                        'max': [],
                        'average': []
                    },
                    'first': {
                        'date': None,
                        'price': 0
                    },
                    'last': {
                        'date': None,
                        'price': 0
                    }
                }
            dicc[category]['counts'] += 1
            dicc[category]['made']['brands'].append(brand)
            dicc[category]['made']['origins'].add(origin)
            dicc[category]['weight'].append(count)

            records = j.get('records', [])

            first_price = records[0].get('price', 0)
            first_date = records[0].get('date', 0)

            if dicc[category]['first']['date'] is None:
                dicc[category]['first']['date'] = first_date
            dicc[category]['first']['price'] += first_price

            last_price = records[-1].get('price', 0)
            last_date = records[-1].get('date', 0)

            if dicc[category]['last']['date'] is None:
                dicc[category]['last']['date'] = last_date
            dicc[category]['last']['price'] += last_price

            dicc[category]['range']['min'].append(last_price)
            dicc[category]['range']['max'].append(last_price)
            dicc[category]['range']['average'].append(last_price)

    for k,v in dicc.items():
        v['made']['brands'] = len(set(v['made']['brands']))
        v['made']['origins'] = list(v['made']['origins'])

        v['weight'] = Moda(v['weight'])

        v['range']['min'] = min(v['range']['min'])
        v['range']['max'] = max(v['range']['max'])
        v['range']['average'] = sum(v['range']['average']) // len(v['range']['average'])

        v['first']['price'] = (v['first']['price'] // v['counts']) / v['weight']
        v['last']['price'] = v['last']['price'] // v['counts'] / v['weight']

    with open('.//data//basket.json', 'w', encoding='utf-8') as file:
        json.dump(dicc, file, ensure_ascii=False, indent=4)

basket = OpenJSON('./data/basket.json')
""" ------------------------------------------------------ """
def Income():    
    """
    Genera una estructura JSON con los datos:
        - mínimo  
        - máximo  
        - promedio  
    """
    values = [i.get('salary', 0) for i in salaries]
    dicc = {
        'min': min(values),
        'max': max(values),
        'average': AverageList(values)
    }
    with open('./data/income.json', 'w', encoding='utf-8') as file:
        json.dump(dicc, file, ensure_ascii=False, indent=4)

income = OpenJSON('./data/income.json')
""" ------------------------------------------------------ """
# Suma total de canasta básica
basket_sum = sum([v['range']['average'] for k,v in basket.items()])
""" ------------------------------------------------------ """
# Rangos de salarios
minimal = income['min']
maximal = income['max']
average = income['average']
""" ------------------------------------------------------ """
""" ------------------------------------------------------ """
""" ------------------------------------------------------ """
""" ------------------------------------------------------ """
""" ------------------------------------------------------ """