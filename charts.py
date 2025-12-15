import matplotlib.pyplot as plt
import numpy as  np
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
def ChartLine(f, v):
    labels = f(v)[0]
    values = f(v)[1]

    plt.subplot()
    plt.plot(labels, values, marker='o', linewidth=2)
    plt.title(f'Evolución del precio del producto: {v}')
    plt.xlabel('Fecha')
    plt.ylabel('Precio (CUP)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
""" ------------------------------------------------------------- """
def ChartBar2(func, f, day):
    labels = func(f, day)[0]
    values = func(f, day)[1]

    plt.subplots()
    plt.barh(labels, values, color='#FFA500')
    plt.xlabel('Días', fontsize=12)
    plt.ylabel('Productos', fontsize=12)
    plt.title('Días Necesarios para Comprar un Producto', fontsize=14, weight='bold')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
""" ------------------------------------------------------------- """
def ChartBarGroup():
    products = [i for i in UnitaryPrice().keys()]
    price = [i for i in UnitaryPrice().values()]
    salaries = [AverageDay(1)] * len(products)

    x = np.arange(len(products))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, price, width, label='Precio Unitario')
    rects2 = ax.bar(x + width/2, salaries, width, label='Salario Promedio')

    ax.set_ylabel('Valor')
    ax.set_title('Canasta Básica vs Salario Promedio')
    ax.set_xticks(x)
    ax.set_xticklabels(products, rotation=45, ha='right')
    ax.legend()
    plt.tight_layout()
    plt.show()
""" ------------------------------------------------------------- """
def ChartBar4():
    precio_cup = ModaCUP()
    precio_usd = ModaUSD()

    categorias = ['CUP', 'USD']
    valores = [precio_cup, precio_usd]
    colores = ['#FF6F61', '#4CAF50']

    plt.subplots()
    plt.bar(categorias, valores, color=colores)
    plt.ylabel('Precio')
    plt.title('CUP vs USD', fontsize=14, weight='bold')
    for i, v in enumerate(valores):
        plt.text(i, v + v*0.01, f'{v:.2f}', ha='center', fontsize=12, weight='bold')
    plt.show()