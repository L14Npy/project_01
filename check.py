import json
import matplotlib.pyplot as plt
import numpy as np
""" -------------------------------------------------------------------- """
# Verifica que MiPymes tiene Coordenadas
def HasLocation():
    with open('./datasets/mipymes.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    mipymes = data.get("mipymes")
    dicc = {}

    for i in range(len(mipymes)):
        name = mipymes[i]["place"]["name"]
        coordinates = mipymes[i]["place"]["location"]["coordinates"]

        if (coordinates["latitude"] is None) and (coordinates["longitude"] is None):
            dicc[name] = coordinates

    for k,v in dicc.items():
        print(f'{k}: {v}')
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """