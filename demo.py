import json
import matplotlib.pyplot as plt
import numpy as np

""" --------------------------------------------------------------------- """
# Promedio Salarial
def AverageSalarie():
    with open('./datasets/salaries.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    salaries = data["salaries"]
    n_salaries = []

    for i in range(len(salaries)):
        salarie = salaries[i]["salarie"]
        n_salaries.append(salarie)

    salaries_sum = 0
    for j in n_salaries:
        salaries_sum += j

    return round(salaries_sum / len(n_salaries), 2)

""" --------------------------------------------------------------------- """
# Promedio Salarial (Diario, Semanal, Mensual)
def AverageSalarieDay(day):
    return round(AverageSalarie() / day, 2)

""" --------------------------------------------------------------------- """
# Promedio Total de un Producto
def AverageProduct(product):
    with open('./datasets/mipymes.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    mipymes = data["mipymes"]
    n_products = []

    for i in range(len(mipymes)):
        products = mipymes[i]["products"]
        
        for j in range(len(products)):
            category = products[j]['category']
            subcategory = products[j]['subcategory']
            records = products[j]["records"]
            
            if category == product and subcategory != 'Aceite de Oliva':
                for k in range(len(records)):
                    price = records[k]["price"]
                    n_products.append(price)

    products_sum = 0
    for m in n_products:
        products_sum += m

    return products_sum / len(n_products)

""" --------------------------------------------------------------------- """
# Promedio Total de la Canasta Básica
def AverageBasket():
    with open('./datasets/mipymes.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    mipymes = data["mipymes"]
    n_baskets = []

    for i in range(len(mipymes)):
        products = mipymes[i]["products"]

        for j in range(len(products)):
            subcategory = products[j]["subcategory"]
            records = products[j]["records"]

            if subcategory != 'Aceite de Oliva':
                for k in range(len(records)):
                    price = records[k]["price"]
                    n_baskets.append(price)

    baskets_sum = 0
    for m in n_baskets:
        baskets_sum += m

    return round(baskets_sum / len(n_baskets), 2)

""" --------------------------------------------------------------------- """
# Días de Salario Necesario
def SalaryDayNecesary(product, day):
    return round(AverageProduct(product) / AverageSalarieDay(day), 2)

""" --------------------------------------------------------------------- """
# Días de Salario de Canasta Básica
def SalaryDayBasket(day):
    return round(AverageBasket() / AverageSalarieDay(day), 2)

""" --------------------------------------------------------------------- """
# Contador de MiPymes & Productos
def count_mipyme_product():
    with open('./datasets/mipymes.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    mipymes = data["mipymes"]
    n_products = []

    for i in range(len(mipymes)):
        products = mipymes[i]["products"]
        n_products.append(len(products))

    print(f'Número de MiPymes: {len(mipymes)}')
    print(f'Cantidad total de productos: {sum(n_products)}')

""" --------------------------------------------------------------------- """
# Nombre de MiPyme, Dirección & Cantidad de Productos
def mipyme_count_product():
    with open('./datasets/mipymes.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    mipymes = data["mipymes"]

    for i in range(len(mipymes)):
        name = mipymes[i]["place"]["name"]
        street = mipymes[i]["place"]["location"]["street"]
        products = mipymes[i]["products"]

        if len(products) >= 10:
            print(f'MiPyme: {name}.\n - Cantidad de productos: {len(products)}')

""" --------------------------------------------------------------------- """
# Promedio Total
def average_total():
    with open('./datasets/mipymes.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    mipymes = data["mipymes"]
    n_prices = []

    for i in range(len(mipymes)):
        products = mipymes[i]["products"]

        for j in range(len(products)):
            records = products[j]["records"]
            
            for k in range(len(records)):
                price = records[k]["price"]
                if price != 0.0:
                    n_prices.append(price)

    return sum(n_prices) // len(n_prices)

""" --------------------------------------------------------------------- """
# Cantidad de Marcas por País de Procedencia
def brand():
    with open('./datasets/mipymes.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    mipymes = data["mipymes"]
    n_brands = []
    n_origins = []

    for i in range(len(mipymes)):
        products = mipymes[i]["products"]
        
        for j in range(len(products)):
            brand = products[j]["brand"]
            origin = products[j]["origin"]
            if (brand not in n_brands) and (brand != None) and (brand != ""):
                n_brands.append(brand)
            if (origin not in n_origins) and (origin != None) and (origin != ""):
                n_origins.append(origin)

    print(f'Cantidad de Marcas: {len(n_brands)} \n- Marcas: {', '.join(n_brands)}')
    print(f'Cantidad de Países: {len(n_origins)} \n- Procedencia: {', '.join(n_origins)}')

""" --------------------------------------------------------------------- """
# Cantidad y tipos de categorías
def categories():
    with open('./datasets/mipymes.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    mipymes = data["mipymes"]
    categories = set()
    subcategories = set()

    for i in range(len(mipymes)):
        products = mipymes[i]["products"]
        
        for j in range(len(products)):
            category = products[j]["category"]
            subcategory = products[j]["subcategory"]
            categories.add(category)
            subcategories.add(subcategory)

    print(f'Cantidad de Categorías: {len(categories)}\n - Categorías: {', '.join(categories)}')
    print(f'Cantidad de Subcategorías: {len(subcategories)}\n - Categorías: {', '.join(subcategories)}')

""" --------------------------------------------------------------------- """
# Cantidad de Productos Internacionales & Nacionales
def export_import():
    with open('./datasets/mipymes.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    mipymes = data["mipymes"]
    internationals = []
    nationals = []

    for i in range(len(mipymes)):
        products = mipymes[i]["products"]

        for j in range(len(products)):
            origin = products[j]["origin"]
            if origin == 'CU':
                nationals.append(origin)
            else:
                internationals.append(origin)

    print(f'Productos internacionales: {len(internationals)}')
    print(f'Productos nacionales: {len(nationals)}')

""" --------------------------------------------------------------------- """
# Porcentaje de Productos Internacionales & Nacionales
def percentage(country):
    with open('./datasets/mipymes.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    mipymes = data["mipymes"]
    n_products = []
    n_internationals = []
    n_nationals = []

    for i in range(len(mipymes)):
        products = mipymes[i]["products"]

        for j in range(len(products)):
            origin = products[j]["origin"]
            n_products.append(origin)

            if origin == country:
                n_nationals.append(origin)
            else:
                n_internationals.append(origin)

    porc_international = (len(n_internationals)/len(n_products))*100
    porc_national = (len(n_nationals)/len(n_products))*100

    print(f'% de Internacionales: {porc_international:.2f}')
    print(f'% de {country}: {porc_national:.2f}')

""" --------------------------------------------------------------------- """
# Marcas y su País de Procedencia
def country_brand():
    with open('./datasets/mipymes.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    mipymes = data["mipymes"]
    dicc = {}

    for i in range(len(mipymes)):
        products = mipymes[i]["products"]

        for j in range(len(products)):
            origin = products[j]["origin"]
            brand = products[j]["brand"]

            if (origin != "") and (origin != None):
                if origin not in dicc:
                    dicc[origin] = set()
                dicc[origin].add(brand)

    for k, v in dicc.items():
        print(f'{k}: {', '.join(v)}')

""" --------------------------------------------------------------------- """
# Categorías por MiPyme
def categories():
    with open('./datasets/mipymes.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    mipymes = data["mipymes"]
    dicc = {}

    for i in range(len(mipymes)):
        name = mipymes[i]["place"]["name"]
        products = mipymes[i]["products"]
        dicc[name] = set()

        for j in range(len(products)):
            category = products[j]["category"]
            dicc[name].add(category)

    for k, v in dicc.items():
        print(f'{k}: {v}')

""" --------------------------------------------------------------------- """
# Subcategorías por MiPyme
def subcategories():
    with open('./datasets/mipymes.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    mipymes = data["mipymes"]
    dicc = {}

    for i in range(len(mipymes)):
        name = mipymes[i]["place"]["name"]
        products = mipymes[i]["products"]
        dicc[name] = set()

        for j in range(len(products)):
            subcategory = products[j]["subcategory"]
            dicc[name].add(subcategory)

    for k, v in dicc.items():
        print(f'{k}: {v}')

""" --------------------------------------------------------------------- """
# Cantidad de Productos por País de Procedencia
def origin_x_product():
    with open('./datasets/mipymes.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    mipymes = data["mipymes"]
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

    for _ in range(7):
        max_key = None
        max_value = -1

        for k, v in counter.items():
            if v > max_value:
                max_value = v
                max_key = k

        print(f'{max_key}: {max_value}')
        del counter[max_key]

""" --------------------------------------------------------------------- """