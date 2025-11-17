import json
import matplotlib.pyplot as plt
import numpy as np
""" -------------------------------------------------------------------- """
def SAD(day):
    # Salario Promedio Diario
    with open('./datasets/salaries.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    salaries = data.get("salaries")
    n_salarie = []
    
    for i in range(len(salaries)):
        salarie = salaries[i].get("salarie")
        n_salarie.append(salarie)

    average = (sum(n_salarie) // len(n_salarie)) // day
    return average
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """