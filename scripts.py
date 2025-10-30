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
# Cantidad de Marcas por País de Procedencia
def brand_country():
    with open('./datasets/mipymes.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    mipymes = data["mipymes"]

    br = []
    mx = []
    es = []
    ma = []
    pol = []
    us = []
    ita = []

    for i in range(len(mipymes)):
        products = mipymes[i]["products"]
        
        for j in range(len(products)):
            origin = products[j]["origin"]
            brand = products[j]["brand"]
            if origin == "BR":
                if (brand not in br) and (brand != None) and (brand != ""):
                    br.append(brand)
            elif origin == "MX":
                if (brand not in mx) and (brand != None) and (brand != ""):
                    mx.append(brand)
            elif origin == "ES":
                if (brand not in es) and (brand != None) and (brand != ""):
                    es.append(brand)
            elif origin == "MA":
                if (brand not in ma) and (brand != None) and (brand != ""):
                    ma.append(brand)
            elif origin == "POL":
                if (brand not in pol) and (brand != None) and (brand != ""):
                    pol.append(brand)
            elif origin == "US":
                if (brand not in us) and (brand != None) and (brand != ""):
                    us.append(brand)
            elif origin == "ITA":
                if (brand not in ita) and (brand != None) and (brand != ""):
                    ita.append(brand)

    print(f'Brasil: {len(br)} \n- Marcas: {', '.join(br)}')
    print(f'México: {len(mx)} \n- Marcas: {', '.join(mx)}')
    print(f'España: {len(es)} \n- Marcas: {', '.join(es)}')
    print(f'Malasia: {len(ma)} \n- Marcas: {', '.join(ma)}')
    print(f'Polonia: {len(pol)} \n- Marcas: {', '.join(pol)}')
    print(f'Estados Unidos: {len(us)} \n- Marcas: {', '.join(us)}')
    print(f'Italia: {len(ita)} \n- Marcas: {', '.join(ita)}')

""" --------------------------------------------------------------------- """
""" --------------------------------------------------------------------- """
""" --------------------------------------------------------------------- """