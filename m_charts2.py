from m_normalize import *
import matplotlib.pyplot as plt
import numpy as np
""" ----------------------------------------- """
def ChartAverageProductsD():
    products = [i for i in AverageProducts().keys()]
    averages = [i for i in AverageProducts().values()]
    plt.subplots(figsize=(10,6))

    bars = plt.bar(
        products,
        averages,
        edgecolor='black',
        linewidth=1
    )

    plt.title('Precio promedio por producto', fontsize=14, fontweight='bold')
    plt.xlabel('Productos', fontsize=12)
    plt.ylabel('Precio (CUP)', fontsize=12)
    plt.xticks(rotation=40, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f'{height:.2f}',
            ha='center',
            va='bottom',
            fontsize=9,
            fontweight="bold"
        )
    plt.tight_layout()
    plt.show()
""" ----------------------------------------- """
def ChartVariabilityPricesD():
    products = [i for i in ListProducts().keys()]
    prices = [i for i in ListProducts().values()]

    plt.figure(figsize=(10, 6))
    violins = plt.violinplot(
        prices,
        showmeans=True,
        showmedians=True,
        showextrema=True
    )
    
    for body in violins['bodies']:
        body.set_facecolor('#7DA7D9')
        body.set_edgecolor('black')
        body.set_alpha(0.7)

    violins['cmeans'].set_color('red')
    violins['cmedians'].set_color('black')
    violins['cbars'].set_linewidth(1)

    plt.title("Distribución de precios por producto", fontsize=14)
    plt.xlabel("Productos", fontsize=11)
    plt.ylabel("Precio (CUP)", fontsize=11)

    plt.xticks(range(1, len(products) + 1), products, rotation=45, ha='right')

    plt.grid(axis='y', linestyle='--', alpha=0.4)
    plt.tight_layout()
    plt.show()
""" ----------------------------------------- """
def ChartCostBasketD():
    labels = ['Canasta básica', 'Salario promedio']
    values = [CostBasket(), AverageSalarie(1)]

    plt.figure(figsize=(10,6))
    bars = plt.bar(labels, values, width=0.5)

    plt.title('Canasta básica vs Salario promedio', fontsize=14, fontweight='bold')
    plt.ylabel('Precios (CUP)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f'{height:,.0f}',
            ha='center',
            va='bottom',
            fontsize=11,
            fontweight="bold"
        )
    plt.ylim(0, max(values) * 1.15)
    plt.tight_layout()
    plt.show()
""" ----------------------------------------- """
def ChartCostBasket2D():
    data = CostBasket2()
    products = list(data.keys())
    prices = list(data.values())
    products, prices = zip(*sorted(zip(products, prices), key=lambda x: x[1]))

    plt.figure(figsize=(10, 6))
    bars = plt.barh(products, prices)
    avg_salary = AverageSalarie(1)
    plt.axvline(
        x=avg_salary,
        linestyle='--',
        linewidth=2,
        color='red',
        label='Salario promedio'
    )
    for bar in bars:
        width = bar.get_width()
        plt.text(
            width + avg_salary * 0.01,
            bar.get_y() + bar.get_height() / 2,
            f'{width:.0f}',
            va='center'
        )
    plt.title('Costo de productos vs Salario promedio', fontsize=14)
    plt.xlabel('Costo mensual (CUP)', fontsize=12)
    plt.ylabel('Productos', fontsize=12)
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()
""" ----------------------------------------- """
def ChartPercetSalaryD():
    data = PercentSalary()
    products = list(data.keys())
    percents = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.bar(products, percents)

    plt.title('Porcentaje del salario necesario', fontsize=14, pad=15)
    plt.ylabel('Porcentaje (%)', fontsize=12)
    plt.xlabel('Producto', fontsize=12)

    plt.xticks(rotation=40, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    for i, value in enumerate(percents):
        plt.text(i, value, f'{value:.1f}%', ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.show()
""" ----------------------------------------- """
""" ----------------------------------------- """
""" ----------------------------------------- """
""" ----------------------------------------- """
""" ----------------------------------------- """