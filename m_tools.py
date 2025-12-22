from m_normalize import *
""" ----------------------------------------- """
def Moda(array:list):
    repeat = 0
    moda = None
    for i in range(len(array)):
        counter = 0
        for j in range(len(array)):
            if array[i] == array[j]:
                counter += 1
        if counter > repeat:
            repeat = counter
            moda = array[i]
    return moda
""" ----------------------------------------- """
def Basket(file) -> dict:
    """
    Guarda en un archivo JSON la canasta de los
    productos con su gramaje
    """
    dicc = {}
    for k,v in UnitaryProducts().items():
        dicc[k] = Moda(v)
    with open(f'./data/{file}', 'w', encoding='utf-8') as f:
        json.dump(dicc, f, ensure_ascii=False, indent=2)
""" ----------------------------------------- """
""" ----------------------------------------- """
""" ----------------------------------------- """