# Precios en tiempos de cólera

#### El salario cubano frente al costo de la canasta básica en MiPymes (Minoristas).

En Cuba, el **precio** es sinónimo de decisión: determina qué puede comprar una persona con su salario en un mercado donde los precios suben sin límite. Entonces surge la pregunta: **¿Puede un cubano de la clase trabajadora adquirir los alimentos básicos?**.

## 1\. Introducción

La economía cubana ha experimentado transformaciones que han impactado en el costo de vida de la población. El surgimiento y expansión de las Micro, Pequeñas y Medianas Empresas (MiPymes), particularmente en el sector del comercio minorista, ha encarecido los precios de los alimentos.

El salario de la clase trabajadora se enfrenta a un entorno de precios desorbitantes, donde la alimentación se convierte en el problema fundamental.

---

## 2\. Objetivo del proyecto

### Objetivo general

Analizar si el salario promedio del trabajador cubano permite adquirir la canasta alimentaria, a partir de precios en MiPymes (Minorista).

### Objetivos específicos

- Recopilar y estructurar datos de precios de productos básicos en MiPymes.  
- Analizar la variabilidad de precios entre distintas MiPymes.  
- Calcular métricas que relacionen precios y **salario promedio**.  
- Evaluar la capacidad de compra del **salario promedio**.  
- Comunicar los resultados a través de visualizaciones coherentes dentro de un storytelling.

---

## 3. Fenómeno analítico

El fenómeno analizado corresponde a la **capacidad adquisitiva del ingreso laboral**, evaluada a partir de la relación entre los **niveles salariales mensuales** y el costo real de los productos que conforman la **canasta básica** de alimentación.

Este fenómeno se manifiesta en los siguientes aspectos:

- La **cantidad máxima de unidades de consumo** que puede adquirir un trabajador en función de su salario y los precios normalizados de los productos.  

- El **esfuerzo laboral requerido**, medido en **días de trabajo**, necesario para la adquisición de bienes alimentarios esenciales.  

- La existencia de **brechas de accesibilidad** entre distintos productos, aun cuando pertenecen a la misma categoría de consumo.

---

## 4\. Fuentes de datos

Se utilizó **tres fuentes de datos independientes**, estructuradas en formato **JSON**.

---

### 4.1 Archivo `pymes.json` – Precios de productos en MiPymes

Contiene la información recopilada de **30 MiPymes** dedicadas al comercio minorista.

```json
[
    {
        "id": "pyme-01",
        "name": "mercadito",
        "currency": "cup",
        "town": "plaza de la revolución",
        "address": {
            "street": "calle j e/ calz. & 9na",
            "location": {
                "latitude": 23.1,
                "longitude": -18.1
            }
        },
        "products": [
            {
                "code": "",
                "category": "picadillo",
                "subcategory": "pollo",
                "unit": "kg",
                "count": 0.4,
                "package": 1.0,
                "brand": "la favorita",
                "origin": "brasil",
                "records": [
                    {
                        "date": "2025-01-01",
                        "price": 350.0
                    }
                ]
            }
        ]
    }
]
```

#### Estructura general

- Cada MiPyme es representada como un objeto dentro de **[]**.  
- Contiene una lista de productos comercializados (mínimo 10).

#### Estructura de producto

Cada producto incluye:

- Categoría: str()
- Subcategoría: str()
- Unidad de medida: float()
- Marca y origen: str()
- Precio: float()
- Registros históricos de pfecha: str()

Esta estructura permite:

- Calcular precios promedio.  
- Analizar dispersión de precios.  
- Realizar comparaciones entre establecimientos.

---

### 4.2 Archivo `products.json` – Producto básicos

El archivo define los **productos básicos** y su consumo mensual recomendado, expresado en **"u/kg/lt"**.

```json
"arroz": {
    "unit": "kg",
    "count": 1.0,
    "days": 5.13859682661059,
    "normalize": 840.0,
    "access": 5.838169642857143,
    "first": {
        "average": 807.027027027027,
        "date": "2025-10-11"
    },
    "last": {
        "average": 840.0,
        "date": "2025-12-11"
    },
    "range": {
        "min": 550.0,
        "max": 1850.0
    }
}
```

#### Justificación

- Sirve como referencia normativa.  
- Permite evaluar si el salario cubre las necesidades mínimas.  
- No depende de precios, sólo de cantidades.

Es clave para vincular el análisis económico con una noción de necesidad básica.

---

### 4.3 Archivo `salaries.json` – Salarios por categoría laboral

Contiene los salarios mensuales organizados por categorías laborales oficiales.

```json
[
    {
        "category": "I",
        "salary": 2100,
        "source": "gaceta oficial"
    }
]
```

#### Campos

- Categoría laboral.  
- Salario mensual en CUP.
- Fuente obtenida

Se utiliza el **salario promedio**, como valor representativo del ingreso del trabajador.

---

## 5\. Estructuras

### 5.1 Módulos

Las funciones del proyecto se encuentran organizadas en archivos `.py`, dentro de la carpeta `modules`.

### 5.2 Archivo `normalize.py` \- Procesamiento de datos

#### Justificación

Constituye la **funcionalidad** del proyecto, siendo responsable de la **lectura, estructura, agregación y análisis** de la información de los archivos `JSON`. Su función es **transformar datos crudos a datos cuantitativos**, que se utilizan para evaluar costos, salarios, y capacidad adquisitiva.

### 5.3 Archivo `charts.py` \- Visualización

#### Justificación

Transforma los **indicadores numéricos** obtenido tras normalizar en **representaciones visuales**, coherentes de acuerdo al **storytelling**

---

### 5.4 Notebook: `story.ipynb`

- Importar funciones.  
- Ejecutar las celdas.  
- Construir el storytelling.  
- Integrar texto, gráficos y resultados.

---

## 6. Resultados

A partir del análisis comparativo entre los **niveles salariales** y los **precios reales de los alimentos**, se obtienen los siguientes resultados:

- El **precio promedio** resulta ser una métrica insuficiente para evaluar la accesibilidad real de los productos.

- La normalización de precios por unidad de medida revela que, en varios casos, la adquisición de un solo producto implica un esfuerzo laboral equivalente a uno o más **días de trabajo**.

- Las visualizaciones construyen una narrativa progresiva que traduce valores monetarios en **unidades comprables y tiempo de trabajo**, permitiendo interpretar el impacto económico desde una perspectiva tangible y socialmente significativa.

Los resultados se presentan de manera progresiva mediante visualizaciones integradas en el archivo `story.ipynb`.

---

## 7\. Instrucciones

Pasos:

- Abrir el archivo `story.ipynb`.  
- Ejecutar todas las celdas.

Requisitos:

- Python 3x.  
- Instalar biblioteca: `pip install matplotlib`.

---

## 8\. Consideraciones finales

Este reporte complementa al archivo `story.ipynb` y cumple con los requisitos académicos establecidos para el proyecto de **Introducción a la Ciencia de Datos**.

---

