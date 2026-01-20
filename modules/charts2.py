from modules.normalize import *
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
    color = ['red', 'green']

    plt.figure(figsize=(10,6))
    bars = plt.bar(labels, values, width=0.5, color=color)

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
def ChartCostBasket2D(day):
    products = [i for i in CostBasket2().keys()]
    prices = [i for i in CostBasket2().values()]

    plt.figure(figsize=(10,6))

    bars = plt.barh(products, prices)
    plt.axvline(
        x=AverageSalarie(day),
        linestyle='--',
        linewidth=2,
        label=f'Salario promedio: {AverageSalarie(day):.0f} CUP',
        color='red'
    )
    for i in bars:
        width = i.get_width()
        plt.text(
            width + max(prices) * 0.001,
            i.get_y() + i.get_height() / 2,
            f'{width:.0f}',
            va='center',
            fontsize=10,
            fontweight='bold'
        )

    plt.title('Costo de productos vs salario promedio', fontsize=14)
    plt.xlabel('Costo mensual (CUP)')
    plt.ylabel('Producto')
    plt.grid(axis='x', linestyle='--', alpha=0.8)
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
def ChartMaxUnitsPlotD(day: int):
    """
    Gráfica la cantidad máxima de cada producto
    que puede comprarse con el salario promedio
    """
    products = [i for i in MaxUnits(day).keys()]
    units = [i for i in MaxUnits(day).values()]

    plt.figure(figsize=(10,6))
    plt.hlines(
        y=products,
        xmin=0,
        xmax=units,
        linewidth=3,
        alpha=0.6
    )
    plt.scatter(
        units,
        products,
        s=80,
        zorder=3
    )
    for i in range(len(units)):
        plt.text(units[i] + max(units) * 0.02, products[i], f"{units[i]:.0f} unidades", va="center", fontweight='bold', fontsize=10)

    plt.xlabel("Cantidad máxima comprable (unidades)", fontsize=12)
    plt.ylabel("Producto")
    plt.title("Cantidad de productos comprables \ncon el salario promedio mensual", fontsize=14)
    plt.grid(axis="x", linestyle="--", alpha=0.9)
    plt.tight_layout()
    plt.show()
""" ----------------------------------------- """
def ChartNecesaryDaysPlotD(day):
    products = [i for i in NecesaryDays(day).keys()]
    days = [i for i in NecesaryDays(day).values()]
    colors = ['green' if d <= day else 'red' for d in days]

    plt.figure(figsize=(10, 6))
    plt.scatter(
        days,
        products,
        s=120,
        alpha=0.8,
        c=colors
    )
    plt.axvline(
        x=day,
        linestyle='--',
        linewidth=2,
        label=f'{day} días laborales',
        color='red'
    )
    for i in range(len(days)):
        plt.text(
            days[i] + 1,
            products[i],
            f'{days[i]:.0f} días',
            va='center',
            fontsize=10,
            fontweight='bold'
        )

    plt.xlabel('Días laborales necesarios', fontsize=12)
    plt.ylabel('Producto', fontsize=12)
    plt.title(
        f'Días laborales necesarios para adquirir productos\n'
        f'(Referencia: {day} días disponibles)',
        fontsize=14
    )

    plt.grid(axis='x', linestyle='--', alpha=0.9)
    plt.legend()
    plt.tight_layout()
    plt.show()
""" ----------------------------------------- """
""" ----------------------------------------- """
""" ----------------------------------------- """