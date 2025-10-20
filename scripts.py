import json

""" --------------------------------------------------------------------- """

def count_mipymes():
    with open('./datasets/mipyme_dataset.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f'Número de MiPymes: {len(data["mipymes"])}')

""" --------------------------------------------------------------------- """