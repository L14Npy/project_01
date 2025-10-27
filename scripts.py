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
""" --------------------------------------------------------------------- """
""" --------------------------------------------------------------------- """
""" --------------------------------------------------------------------- """