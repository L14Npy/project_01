from normalize import *
import matplotlib.pyplot as plt
""" -------------------------------------------------------------------- """
def NI(made, path=path1):
    # Genera una gráfica de tipo pastel de porcentajes de productos "Nacionales/Internacionales"
    made = made.upper()
    mipymes = OpenJSON(path).get("mipymes")
    n_national = []
    n_international = []

    for i in range(len(mipymes)):
        products = mipymes[i].get("products")

        for j in range(len(products)):
            origin = products[j]["origin"]

            if origin is None or origin == '':
                continue
            if origin == made:
                n_national.append(origin)
            else:
                n_international.append(origin)

    labels = [f'{made}', 'Resto']
    sizes = [len(n_national), len(n_international)]
    explode = [0, 0.1]

    plt.figure(figsize=(5,5))
    plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%')
    plt.title(f"Distribución de Productos: {made} vs Resto")
    plt.axis("equal")
    plt.show()
""" -------------------------------------------------------------------- """
def BarOP(n):
    labels = [i for i in OrderDicc('origin', n).keys()]
    values = [i for i in OrderDicc('origin', n).values()]

    plt.figure(figsize=(8,5))
    plt.bar(labels, values)
    plt.title(f'Top {n} Orígenes de Productos')
    plt.ylabel('Cantidades')
    plt.xlabel('Paises')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.4)
    plt.show()
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """
""" -------------------------------------------------------------------- """