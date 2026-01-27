from modules.normalize import *
""" -------------------------------------- """
def SalaryCategories(start, end):
    if end > 32:
        return print('Rango máximo 32')
    categories = [i.get('category') for i in salaries[start:end]]
    values = [i.get('salary') for i in salaries[start:end]]

    plt.subplots(figsize=(12,6))
    plt.bar(categories, values, color='skyblue', edgecolor='blue')
    plt.title('Rango salarial', fontsize=18)

    plt.xlabel('Salarios', fontsize=14)
    plt.xticks(rotation=45)
    plt.ylabel('Precio (CUP)', fontsize=14)

    for c,v in enumerate(values):
        plt.text(c, v+80, f'{v:.2f} CUP', ha='center', fontsize=10, fontweight='bold')

    plt.tight_layout()
    plt.show()
""" -------------------------------------- """
def MinMaxAve():
    ranges = [i for i in Salaries().keys()]
    values = [i for i in Salaries().values()]

    plt.subplots(figsize=(12,6))
    plt.bar(ranges, values, color='skyblue', edgecolor='blue')
    plt.title('Salario Min/Promedio/Max', fontsize=18)

    plt.xlabel('Salarios', fontsize=14)
    plt.ylabel('Precio (CUP)', fontsize=14)

    for r,v in enumerate(values):
        plt.text(r, v+100, f'{v:.2f} CUP', ha='center', fontsize=12, fontweight='bold')

    plt.tight_layout()
    plt.show()
""" -------------------------------------- """
def AverageProducts(unit):
    products = [f'{str(k).capitalize()} ({v['count']} {v['unit']})' for k,v in unit.items()]
    values = [v['last']['average'] for k,v in unit.items()]

    if len(products) > 2:
        plt.subplots(figsize=(12,6))
        plt.bar(products, values, color='skyblue', edgecolor='blue')
        plt.title('Precios/Promedio', fontsize=16)
        plt.xlabel('Productos', fontsize=12)
        plt.xticks(rotation=30)
        plt.ylabel('Precio promedio (CUP)', fontsize=12)
        plt.tight_layout

        for p,v in enumerate(values):
            plt.text(p, v+50, f"{v:.2f} CUP", ha='center', fontsize=7, fontweight='bold')

    plt.axhline(y=Salaries()['min'], color='red', linestyle='--', linewidth=3, label='Salario mínimo (CUP)')
    plt.legend()
    plt.show()
""" -------------------------------------- """
def Dispertion(unit):
    products = [f'{str(k).capitalize()} ({v['count']} {v['unit']})' for k,v in unit.items()]
    minimal = [v['range']['min'] for k,v in unit.items()]
    maximal = [v['range']['max'] for k,v in unit.items()]
    average = [v['last']['average'] for k,v in unit.items()]

    if len(products) > 2:
        plt.subplots(figsize=(12,6))
        for i, p in enumerate(products):
            plt.plot([i,i], [minimal[i], maximal[i]], color='gray', linewidth=10, alpha=0.6)

        plt.scatter(range(len(products)), average, color='blue', zorder=5, label='Precio promedio (CUP)')
        plt.scatter(range(len(products)), maximal, color='red', zorder=5, label='Precio máximo (CUP)')
        plt.scatter(range(len(products)), minimal, color='green', zorder=5, label='Precio mínimo (CUP)')

        plt.xticks(range(len(products)), products, rotation=30)
        plt.ylabel('Precio (CUP)')
        plt.title('Dispersión de precios', fontsize=16)
        plt.tight_layout()
    else:
        plt.subplots()
        for i, p in enumerate(products):
            plt.plot([i,i], [minimal[i], maximal[i]], color='gray', linewidth=10, alpha=0.6)

        plt.scatter(range(len(products)), average, color='blue', zorder=5, label='Precio promedio (CUP)')
        plt.scatter(range(len(products)), maximal, color='red', zorder=5, label='Precio máximo (CUP)')
        plt.scatter(range(len(products)), minimal, color='green', zorder=5, label='Precio mínimo (CUP)')

        plt.xticks(range(len(products)), products)
        plt.ylabel('Precio (CUP)')
        plt.title('Dispersión de precios', fontsize=16)

    plt.axhline(y=Salaries()['min'], color='red', linestyle='--', linewidth=3, label='Salario mínimo')
    plt.legend()
    plt.show()
""" -------------------------------------- """
def MiPymes():
    text = [str(i).capitalize() for i in mipymes]
    ave = [mipymes[i]['ave_pyme'] for i in mipymes]
    
    plt.subplots(figsize=(12, len(text)*0.3))
    plt.barh(text, ave, color='skyblue', edgecolor='blue')
    plt.title('Costo promedio por MiPyme', fontsize=16)
    plt.xlabel('CUP', fontsize=12)
    plt.ylabel('MiPymes', fontsize=12)

    plt.axvline(x=Salaries()['min'], color='red', linestyle='--', linewidth=2, label='Salario mínimo (CUP)')
    for t,v in enumerate(ave):
        plt.text(v+20, t, f'{v:.2f} CUP', va='center', fontsize=10)

    plt.legend()
    plt.tight_layout()
    plt.show()
""" -------------------------------------- """
def Days(day):
    names = [f'{k} ({v['count']} {v['unit']})' for k,v in Products(sizes, day, 1).items()]
    days = [v.get('days') for k,v in Products(sizes, day, 1).items()]

    plt.subplots(figsize=(12, 6))
    plt.barh(names, days, color='skyblue', edgecolor='blue')
    plt.title(f'Días necesarios', fontsize=16)
    plt.xlabel('Días de salario', fontsize=12)
    plt.ylabel('Productos', fontsize=12)

    for n,d in enumerate(days):
        plt.text(d+0.01, n, f'{(d*10):.2f} Días', va='center', fontsize=10)

    plt.show()
""" -------------------------------------- """
def Individual(product):
    product = product.lower()
    units = [f'{v['subcategory'].capitalize()} {str(k)} {v['unit']}' for k,v in IndividualProducts(product).items()]
    prices = [v['price'] for k,v in IndividualProducts(product).items()]
    
    plt.subplots(figsize=(12,6))
    plt.bar(units, prices, color='skyblue', edgecolor='blue')
    plt.title(f'Precios/Promedio - {product.capitalize()}', fontsize=16)
    plt.xlabel('Productos', fontsize=12)
    plt.ylabel('Precio promedio (CUP)', fontsize=12)
    plt.xticks(rotation=15)
    plt.tight_layout

    for p,v in enumerate(prices):
        plt.text(p, v+20, f"{v:.2f} CUP", ha='center', fontsize=8, fontweight='bold')

    plt.show()
""" -------------------------------------- """
def NormalizeProducts(unit):
    products = [f'{str(k).capitalize()} ({v['unit']}/cup)' for k,v in unit.items()]
    values = [v['normalize'] for k,v in unit.items()]

    if len(products) > 2:
        plt.subplots(figsize=(12,6))
        plt.bar(products, values, color='skyblue', edgecolor='blue')
        plt.title('Precios/Normalizado', fontsize=16)
        plt.xlabel('Productos', fontsize=12)
        plt.xticks(rotation=30)
        plt.ylabel('Precio promedio (CUP)', fontsize=12)
        plt.tight_layout

        for p,v in enumerate(values):
            plt.text(p, v+50, f"{v:.2f} CUP", ha='center', fontsize=6, fontweight='bold')

    plt.axhline(y=Salaries()['min'], color='red', linestyle='--', linewidth=3, label='Salario mínimo (CUP)')
    plt.axhline(y=Salaries()['average'], color='blue', linestyle='--', linewidth=3, label='Salario promedio (CUP)')
    plt.legend()
    plt.show()
""" -------------------------------------- """
def Access(d):
    names = [f"{k} ({v['count']} {v['unit']})" for k, v in Products(sizes, 1, d).items()]
    access = [v['access'] for k, v in Products(sizes, 1, d).items()]

    if d == 1:
        title = 'Mensual'
    elif d >= 4:
        title = 'Semanal'
    elif d >= 15:
        title = 'Quincenal'
    elif d >= 22:
        title = 'Diario'

    plt.subplots(figsize=(12, 6))
    plt.barh(names, access)

    plt.axvline(
        x=1,
        linestyle='--',
        linewidth=2,
        color='red',
        label='Accesibilidad (1 unidad)'
    )

    plt.title(f'Accesibilidad - {title}', fontsize=16)
    plt.xlabel('Unidades adquiribles', fontsize=12)
    plt.ylabel('Productos', fontsize=12)

    for n,a in enumerate(access):
        plt.text(a+0.1, n, f'{a:.0f}', va='center', fontsize=10, fontweight='bold')

    plt.legend()
    plt.tight_layout()
    plt.show()
""" -------------------------------------- """
def NecesaryDays(d):
    names = [f"{k} ({v['count']} {v['unit']})" for k, v in Products(sizes, 1, d).items()]
    access = [v['days'] for k, v in Products(sizes, 1, d).items()]

    plt.subplots(figsize=(12, 6))
    plt.barh(names, access)

    plt.axvline(
        x=30,
        linestyle='--',
        linewidth=2,
        color='red',
        label='Días laborales (30 días)'
    )

    plt.title('Días necesarios', fontsize=16)
    plt.xlabel('Días laborables', fontsize=12)
    plt.ylabel('Productos', fontsize=12)

    for n,a in enumerate(access):
        plt.text(a+0.1, n, f'{a:.0f} días laborales', va='center', fontsize=10, fontweight='bold')

    plt.legend()
    plt.tight_layout()
    plt.show()
""" -------------------------------------- """
def TimeTravel1(product):
    dates = [k for k,v in TimeSeries(product).items()]
    prices1 = [v['price'] for k,v in TimeSeries(product).items()]
    prices2 = [v['price'] for k,v in elToque().items()]

    plt.subplots(figsize=(12,6))
    plt.plot( dates, prices1, marker='o', linewidth=2, label='Precio promedio MiPyme (CUP)')
    plt.xlabel('Fecha')
    plt.ylabel('Precio promedio (CUP)')
    plt.tick_params(axis='y')

    plt.twinx()
    plt.plot( dates, prices2, marker='s', linewidth=2, label='Cambio informal (CUP)')
    plt.ylabel('USD informal')
    plt.tick_params(axis='y')

    plt.title('Evolución temporal: Precios (producto) vs Cambio informal', fontsize=16)
    plt.tight_layout()
    plt.show()
""" -------------------------------------- """
def TimeTravel(product):
    ts_mipyme = TimeSeries(product)
    ts_usd = elToque()

    dates = [i for i in ts_mipyme.keys()]
    prices1 = [v['price'] for v in ts_mipyme.values()]
    prices2 = [v['price'] for v in ts_usd.values()]

    fig, ax1 = plt.subplots(figsize=(12,6))

    ax1.plot(
        dates,
        prices1,
        color='steelblue',
        marker='o',
        linewidth=2,
        label='Precio promedio MiPyme (CUP)'
    )
    ax1.set_xlabel('Fecha')
    ax1.set_ylabel('Precio promedio (CUP)', color='steelblue')
    ax1.tick_params(axis='y', labelcolor='steelblue')

    ax2 = ax1.twinx()
    ax2.plot(
        dates[:len(prices2)],
        prices2,
        color='firebrick',
        marker='s',
        linestyle='--',
        linewidth=2,
        label='USD informal (El Toque)'
    )
    ax2.set_ylabel('USD informal (CUP)', color='firebrick')
    ax2.tick_params(axis='y', labelcolor='firebrick')

    plt.title(f'Evolución temporal: {product} vs USD informal',fontsize=16)

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(
        lines1 + lines2,
        labels1 + labels2,
        loc='upper left'
    )

    plt.tight_layout()
    plt.show()
""" -------------------------------------- """
""" -------------------------------------- """