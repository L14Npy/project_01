import json
import matplotlib.pyplot as plt
""" -------------------------------------- """
def OpenJSON(path:str):
    """
    Abre archivos de formato JSON  
    """
    with open(path, 'r', encoding='utf-8') as f:
        datas = json.load(f)
    return datas

pymes = OpenJSON('./data/pymes.json')
salaries = OpenJSON('./data/salaries.json')
""" -------------------------------------- """
def AverageDays(array:list, days:int):
    """
    Promedio diario  
    """
    return (sum(array) / len(array)) / days
""" -------------------------------------- """
def Salaries():
    """
    Mínimo, máximo y promedio  
    """
    salarie = [i.get('salary') for i in salaries]
    dicc = {
        'min': min(salarie),
        'average': AverageDays(salarie, 1),
        'max': max(salarie),
    }
    return dicc
""" -------------------------------------- """
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
""" -------------------------------------- """
""" -------------------------------------- """
def Products2(value, sizes):
    dicc = {}
    for i in pymes:
        for j in i.get('products', []):
            category = j.get('category')
            subcategory = j.get('subcategory')
            unit = j.get('unit')
            count = j.get('count')
            records = j.get('records', [])
            
            if category == 'infusiones' or subcategory in ['cartón','docena']:
                continue
            if category in sizes:
                if unit == value and count == sizes[category]:
                    if category not in dicc:
                        dicc[category] = {
                            'unit': [],
                            'count': [],
                            'first': {
                                'average': [],
                                'date': records[0]['date'],
                            },
                            'last': {
                                'average': [],
                                'date': records[-1]['date'],
                            },
                            'range': {
                                'min': [],
                                'max': []
                            }
                        }
                    dicc[category]['count'].append(count)
                    dicc[category]['unit'].append(unit)
                    dicc[category]['first']['average'].append(records[0]['price'])
                    dicc[category]['last']['average'].append(records[-1]['price'])
                    dicc[category]['range']['min'].append(records[-1]['price'])
                    dicc[category]['range']['max'].append(records[-1]['price'])
    
    for k,v in dicc.items():
        v['unit'] = Moda(v['unit'])
        v['count'] = Moda(v['count'])
        v['first']['average'] = AverageDays(v['first']['average'], 1)
        v['last']['average'] = AverageDays(v['last']['average'], 1)
        v['range']['min'] = min(v['range']['min'])
        v['range']['max'] = max(v['range']['max'])

    """ with open(f'./data/products_{value}.json', 'w', encoding='utf-8') as f:
        json.dump(dicc, f, ensure_ascii=False, indent=4) """

    return dicc

#kilograms = OpenJSON('data/products_kg.json')
#liters = OpenJSON('data/products_lt.json')
#unities = OpenJSON('data/products_u.json')
""" -------------------------------------- """
def Products(sizes, days, d):
    dicc = {}
    for i in pymes:
        for j in i.get('products', []):
            category = j.get('category')
            subcategory = j.get('subcategory')
            unit = j.get('unit')
            count = j.get('count')
            records = j.get('records', [])
            
            if category == 'infusiones' or subcategory in ['cartón','docena']:
                continue
            if category in sizes:
                if unit == 'kg' and count == sizes[category]:
                    if category not in dicc:
                        dicc[category] = {
                            'unit': [],
                            'count': [],
                            'days': 0,
                            'normalize': 0,
                            'access': 0,
                            'first': {
                                'average': [],
                                'date': records[0]['date'],
                            },
                            'last': {
                                'average': [],
                                'date': records[-1]['date'],
                            },
                            'range': {
                                'min': [],
                                'max': []
                            }
                        }
                    dicc[category]['count'].append(count)
                    dicc[category]['unit'].append(unit)
                    dicc[category]['first']['average'].append(records[0]['price'])
                    dicc[category]['last']['average'].append(records[-1]['price'])
                    dicc[category]['range']['min'].append(records[-1]['price'])
                    dicc[category]['range']['max'].append(records[-1]['price'])

            if category in sizes:
                if unit == 'lt' and count == sizes[category]:
                    if category not in dicc:
                        dicc[category] = {
                            'unit': [],
                            'count': [],
                            'days': 0,
                            'normalize': 0,
                            'access': 0,
                            'first': {
                                'average': [],
                                'date': records[0]['date'],
                            },
                            'last': {
                                'average': [],
                                'date': records[-1]['date'],
                            },
                            'range': {
                                'min': [],
                                'max': []
                            }
                        }
                    dicc[category]['count'].append(count)
                    dicc[category]['unit'].append(unit)
                    dicc[category]['first']['average'].append(records[0]['price'])
                    dicc[category]['last']['average'].append(records[-1]['price'])
                    dicc[category]['range']['min'].append(records[-1]['price'])
                    dicc[category]['range']['max'].append(records[-1]['price'])

            if category in sizes:
                if unit == 'u' and count == sizes[category]:
                    if category not in dicc:
                        dicc[category] = {
                            'unit': [],
                            'count': [],
                            'days': 0,
                            'normalize': 0,
                            'access': 0,
                            'first': {
                                'average': [],
                                'date': records[0]['date'],
                            },
                            'last': {
                                'average': [],
                                'date': records[-1]['date'],
                            },
                            'range': {
                                'min': [],
                                'max': []
                            }
                        }
                    dicc[category]['count'].append(count)
                    dicc[category]['unit'].append(unit)
                    dicc[category]['first']['average'].append(records[0]['price'])
                    dicc[category]['last']['average'].append(records[-1]['price'])
                    dicc[category]['range']['min'].append(records[-1]['price'])
                    dicc[category]['range']['max'].append(records[-1]['price'])
    
    for k,v in dicc.items():
        v['unit'] = Moda(v['unit'])
        v['count'] = Moda(v['count'])
        v['first']['average'] = AverageDays(v['first']['average'], days)
        v['last']['average'] = AverageDays(v['last']['average'], days)
        v['range']['min'] = min(v['range']['min'])
        v['range']['max'] = max(v['range']['max'])

        v['normalize'] = v['last']['average'] / v['count']

        v['access'] = (Salaries()['average'] / d) / v['last']['average']

        v['days'] = 30 / v['access']

    with open(f'./data/products.json', 'w', encoding='utf-8') as f:
        json.dump(dicc, f, ensure_ascii=False, indent=4)

    return dicc

products_json = OpenJSON('./data/products.json')
""" -------------------------------------- """
def Sizes(weight):
    dicc = {}
    for k,v in weight.items():
        dicc[k] = v['count']
    return dicc

sizes = Sizes(products_json)
""" -------------------------------------- """
products = Products(sizes, 1, 1)
#kg = Products('kg', sizes_kg)
#lt = Products('lt', sizes_lt)
#uni = Products('u', sizes_uni)
""" -------------------------------------- """
def Pymes(sizes):
    dicc = {}

    for i in pymes:
        name = i.get('name')
        if name not in dicc:
            dicc[name] = {}

        for j in i.get('products', []):
            category = j.get('category')
            subcategory = j.get('subcategory')
            unit = j.get('unit')
            count = j.get('count')
            records = j.get('records', [])

            if category == 'infusiones' or subcategory in ['cartón', 'docena']:
                continue
            if category in sizes and unit == 'kg' and count == sizes[category]:
                if category not in dicc[name]:
                    dicc[name][category] = {
                        'ave_product': []
                    }
                dicc[name][category]['ave_product'].append(records[-1]['price'])

            if category in sizes and unit == 'lt' and count == sizes[category]:
                if category not in dicc[name]:
                    dicc[name][category] = {
                        'ave_product': []
                    }
                dicc[name][category]['ave_product'].append(records[-1]['price'])

            if category in sizes and unit == 'u' and count == sizes[category]:
                if category not in dicc[name]:
                    dicc[name][category] = {
                        'ave_product': []
                    }
                dicc[name][category]['ave_product'].append(records[-1]['price'])

    for pyme,category in dicc.items():
        for k,v in category.items():
            v['ave_product'] = AverageDays(v['ave_product'], 1)

    for i in dicc:
        sum = 0
        counter = 0
        for j in dicc[i]:
            sum += dicc[i][j]['ave_product']
            counter += 1
        dicc[i]['ave_pyme'] = sum / counter

    """ with open(f'./data/mipymes.json', 'w', encoding='utf-8') as f:
        json.dump(dicc, f, ensure_ascii=False, indent=4) """
    
    return dicc
""" -------------------------------------- """
mipymes = Pymes(sizes)
""" -------------------------------------- """
def IndividualProducts(product):
    dicc = {}
    for i in pymes:
        for j in i.get('products', []):
            category = j.get('category')
            subcategory = j.get('subcategory')
            unit = j.get('unit')
            count = j.get('count')
            brand = j.get('brand')
            origin = j.get('origin')
            records = j.get('records', [])

            if category == 'infusiones' or subcategory in ['cartón','docena']:
                continue
            if category == product:
                if count not in dicc:
                    dicc[count] = {
                        'category': category,
                        'subcategory': subcategory,
                        'unit': unit,
                        'count': count,
                        'normalize': 0,
                        'price': [],
                    }
                dicc[count]['price'].append(records[-1]['price'])

    for k,v in dicc.items():
        v['price'] = AverageDays(v['price'], 1)
        v['normalize'] = v['price'] / v['count']

    """ with open(f'./data/individual_{product}.json', 'w', encoding='utf-8') as file:
        json.dump(dicc, file, ensure_ascii=False, indent=4) """
    
    return dicc
""" -------------------------------------- """
""" -------------------------------------- """
""" -------------------------------------- """
""" -------------------------------------- """
""" -------------------------------------- """