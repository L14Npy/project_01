from m_normalize import *
import matplotlib.pyplot as plt
import numpy as np
""" ----------------------------------------- """
def ChartAverageProducts():
    products = [i for i in AverageProducts().keys()]
    averages = [i for i in AverageProducts().values()]
    
    plt.subplots()
    plt.bar(products, averages)
    plt.title('Precio promedio x producto')
    plt.xlabel('Productos')
    plt.ylabel('Precios (CUP)')
    plt.xticks(rotation=40)
    plt.show()
""" ----------------------------------------- """
def ChartAveragePyme():
    pyme = [i for i in AveragePyme().keys()]
    averages = [i for i in AveragePyme().values()]
    
    plt.subplots()
    plt.bar(pyme, averages)
    plt.title('Precio promedio x MiPyme')
    plt.xlabel('MiPymes')
    plt.ylabel('Precios (CUP)')
    plt.xticks(rotation=40)
    plt.show()
""" ----------------------------------------- """
def ChartCostBasket():
    labels = ['Canasta básica', 'Salario promedio']
    values = [CostBasket(), AverageSalarie(1)]

    plt.subplots()
    plt.bar(labels, values)
    plt.title('Canasta básica VS Salario promedio')
    plt.ylabel('Precios (CUP)')
    plt.show()
""" ----------------------------------------- """
def ChartCostBasket2():
    products = [i for i in CostBasket2().keys()]
    prices = [i for i in CostBasket2().values()]

    plt.subplots()
    plt.barh(products, prices)
    plt.axvline(x=AverageSalarie(1), linestyle='--', linewidth=2, label='Salario promedio', color='red')
    plt.title('Producto VS Salario promedio')
    plt.xlabel('Costo mensual (CUP)')
    plt.legend()
    plt.show()
""" ----------------------------------------- """
def ChartVariabilityPrices():
    products = [i for i in ListProducts().keys()]
    prices = [i for i in ListProducts().values()]

    plt.subplots()
    plt.violinplot(prices, showmeans=True, showextrema=True)
    plt.title("Distribución de precios por producto")
    plt.xlabel("Productos")
    plt.xticks(range(1, len(products)+1), products, rotation=45)
    plt.ylabel("Precio (CUP)")
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.show()
""" ----------------------------------------- """
def ChartPercetSalary():
    products = [i for i in PercentSalary().keys()]
    percents = [i for i in PercentSalary().values()]

    plt.subplots()
    plt.bar(products, percents)
    plt.title('Porcentaje del salario necesario')
    plt.ylabel('Porcentajes')
    plt.xticks(rotation=40)
    plt.show()
""" ----------------------------------------- """
def ChartNecesaryDays(day):
    products = [i for i in NecesaryDays(day).keys()]
    days = [i for i in NecesaryDays(day).values()]

    plt.subplots()
    plt.barh(products, days)
    plt.show()
""" ----------------------------------------- """
""" ----------------------------------------- """