from modules.normalize import *
from modules.vars import *
""" ------------------------------------------------------ """
def ChartSalaries():
    text = [i.get('category') for i in salaries]
    price = [i.get('salary') for i in salaries]

    fig, ax = plt.subplots(figsize=(12,6))
    ax.plot(text, price, color='blue', linestyle='-', marker='o', label='Salarios (CUP)')
    ax.axhline(y=basket_sum, color='red', linestyle='--', linewidth=2, label='Canasta básica')
    plt.title('Salario/Categoría', fontsize=14)
    plt.xlabel('Categorias')
    plt.xticks(rotation=60)
    plt.ylabel('Salarios')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()
""" ------------------------------------------------------ """
def ChartProducts():
    text = [i for i in basket]
    price = [v['range']['average'] for k,v in basket.items()]

    fig, ax = plt.subplots(figsize=(12,6))
    ax.bar(text, price, color='skyblue', edgecolor='blue', label='Precios (CUP)')
    ax.axhline(y=minimal, color='red', linestyle='--', linewidth=2, label='Salario mínimo')
    ax.axhline(y=maximal, color='purple', linestyle='--', linewidth=2, label='Salario máximo')
    ax.axhline(y=average, color='blue', linestyle='--', linewidth=2, label='Salario promedio')
    plt.title('Precio Promedio/Producto', fontsize=16)
    plt.xlabel('Categorías', fontsize=14, fontweight='bold')
    plt.ylabel('Valores (CUP)', fontsize=12)
    plt.xticks(text, rotation=45, ha='right')

    for t, p in enumerate(price):
        plt.text(t, p + 60, f'{p:.2f}', ha='center', fontsize=10, fontweight='bold')

    plt.legend()
    plt.tight_layout()
    plt.show()
""" ------------------------------------------------------ """
def ChartProducts2():
    text = [i for i in basket]
    price = [v['last']['price'] for k,v in basket.items()]

    fig, ax = plt.subplots(figsize=(12,6))
    ax.bar(text, price, color='skyblue', edgecolor='blue', label='Precios (CUP)')
    ax.axhline(y=minimal, color='red', linestyle='--', linewidth=2, label='Salario mínimo')
    ax.axhline(y=maximal, color='purple', linestyle='--', linewidth=2, label='Salario máximo')
    ax.axhline(y=average, color='blue', linestyle='--', linewidth=2, label='Salario máximo')
    plt.title('Precio Promedio/Producto(kg/lt/u)', fontsize=16)
    plt.xlabel('Categorías', fontsize=14, fontweight='bold')
    plt.ylabel('Valores (CUP)', fontsize=12)
    plt.xticks(text, rotation=45, ha='right')

    for t, p in enumerate(price):
        plt.text(t, p + 100, f'{p:.2f}', ha='center', fontsize=10, fontweight='bold')

    plt.legend()
    plt.tight_layout()
    plt.show()
""" ------------------------------------------------------ """
def ChartComparation():
    text = ['Canasta básica', 'Salario promedio']
    price = [basket_sum, average]
    
    fig, ax = plt.subplots()
    ax.bar(text, price, color=['red', 'green'], edgecolor='black', label=['Canasta básica', 'Salario promedio'])
    plt.title('Canasta básica VS Salario promedio', fontsize=16)
    plt.ylabel('Valores (CUP)', fontsize=12)

    for t, p in enumerate(price):
        plt.text(t, p + 200, f'{p:.2f}', ha='center', fontsize=10, fontweight='bold')

    plt.legend()
    plt.show()
""" ------------------------------------------------------ """
def ChartUnits(day):
    text = [i for i in MaxUnits(day).keys()]
    units = [i for i in MaxUnits(day).values()]

    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.barh(text, units, color='skyblue', edgecolor='blue')

    plt.title(f'Unidades máximas', fontsize=14)
    plt.xlabel('Unidades máximas comprables', fontsize=12)

    for bar in bars:
        width = bar.get_width()
        ax.text(width + max(units)*0.01, bar.get_y() + bar.get_height()/2, f'{width:.2f} unidades', va='center', ha='left', fontsize=10)
    
    plt.grid(axis='x', alpha=0.9, linestyle='--')
    plt.show()
""" ------------------------------------------------------ """
def ChartNecesaryDays(day):
    text = [i for i in NecesaryDays(day).keys()]
    units = [i for i in NecesaryDays(day).values()]

    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.barh(text, units, color='skyblue', edgecolor='blue')

    plt.title(f'Día laborales necesarios en {day}', fontsize=14)
    plt.xlabel('Días laborales', fontsize=12)

    for bar in bars:
        width = bar.get_width()
        ax.text(width + max(units)*0.01, bar.get_y() + bar.get_height()/2, f'{width:.0f} días', va='center', ha='left', fontsize=10, fontweight='bold')
    
    plt.axvline(
        x=day,
        linestyle='--',
        linewidth=2,
        label=f'{day} días laborales',
        color='red'
    )

    plt.grid(axis='x', alpha=0.9, linestyle='--')
    plt.show()
""" ------------------------------------------------------ """
""" ------------------------------------------------------ """
""" ------------------------------------------------------ """
""" ------------------------------------------------------ """