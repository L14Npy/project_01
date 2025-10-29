import json

""" --------------------------------------------------------------------- """
# Contador de MiPymes & Productos
def mipymes_products_count():
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
def mipymes_town():
    with open('./datasets/mipymes.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    mipymes = data["mipymes"]

    for i in range(len(mipymes)):
        name = mipymes[i]["place"]["name"]
        street = mipymes[i]["place"]["location"]["street"]
        products = mipymes[i]["products"]

        print(f'MiPyme: {name}.\n - Dirección: {street}.\n - Cantidad de productos: {len(products)}')

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

def brand():
    with open('./datasets/mipymes.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    mipymes = data["mipymes"]
    n_brands = []

    for i in range(len(mipymes)):
        products = mipymes[i]["products"]
        
        for j in range(len(products)):
            brand = products[j]["brand"]
            if (brand not in n_brands) and (brand != None) and (brand != ""):
                n_brands.append(brand)

    print(f'Cantidad de Marcas: {len(n_brands)} \n- Marcas: {', '.join(n_brands)}')

""" --------------------------------------------------------------------- """
""" --------------------------------------------------------------------- """
""" --------------------------------------------------------------------- """
""" --------------------------------------------------------------------- """