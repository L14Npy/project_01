import matplotlib.pyplot as plt
from normalize import *
""" ------------------------------------------------------------- """
def ChartPie(f, k, v):
    labels = [i for i in f(k, v).keys()]
    values = [i for i in f(k, v).values()]

    plt.subplots()
    plt.title(f'Distribución de Productos: CU vs {v.upper()}')
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()
""" ------------------------------------------------------------- """
def ChartPie2(func, f, k, rg):
    labels = [i for i in func(f, k, rg).keys()]
    values = [i for i in func(f, k, rg).values()]

    plt.subplots()
    plt.title(f'Distribución de Productos')
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.show()
""" ------------------------------------------------------------- """
def ChartPie3(f, k):
    values = f(k)

    plt.subplots()
    plt.title(f'Distribución de Productos: Nacionales & Importados')
    plt.pie(values, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()
""" ------------------------------------------------------------- """
def ChartBar(func, f, k, rg):
    x = [i for i in func(f, k, rg).keys()]
    y = [i for i in func(f, k, rg).values()]

    plt.subplots()
    plt.barh(x, y)
    plt.gca().invert_yaxis()
    plt.show()
""" ------------------------------------------------------------- """
""" ------------------------------------------------------------- """
""" ------------------------------------------------------------- """