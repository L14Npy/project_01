# Precios en tiempos de cólera  
#### El salario cubano frente al costo de la canasta básica en MiPymes (Minoristas).

En Cuba, el **precio** es sinónimo de decisión: determina qué puede comprar una persona con su salario en un mercado donde los precios suben sin límite. Entonces surge la pregunta: **¿Puede un cubano de la clase trabajadora adquirir los alimentos básicos?**.

## 1. Introducción

La economía cubana ha experimentado transformaciones que han impactado en el costo de vida de la población. El surgimiento y expansión de las Micro, Pequeñas y Medianas Empresas (MiPymes), particularmente en el sector del comercio minorista, ha encarecido los de precios de la canasta básica.

El salario de la clase trabajadora se enfrenta a un entorno de precios desorbitantes, donde la alimenctación se convierte en el problema fundamental.

---

## 2. Objetivo del proyecto

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

El fenómeno analizado es la capacidad adquisitiva del **salario promedio**, como la relación entre el **ingreso laboral mensual** y el costo de alimentación.

Este fenómeno se manifiesta en:
- La cantidad máxima de alimentos que puede adquirir un trabajador.
- El número de días laborales necesarios para comprar un producto.

El análisis se limita a un enfoque descriptivo, sin modelos predictivos ni inferenciales.

---

## 4. Fuentes de datos

Se utilizó **tres fuentes de datos independientes**, estructuradas en formato **JSON**.

---

### 4.1 Archivo `pymes.json` – Precios de productos en MiPymes

Contiene la información recopilada de **30 MiPymes** dedicadas al comercio minorista.

#### Estructura general

- Cada MiPyme es representada como un objeto.
- Contiene una lista de productos comercializados (mínimo 10).

#### Estructura de producto

Cada producto incluye:
- Categoría y subcategoría.
- Unidad de medida.
- Marca y origen.
- Registros históricos de precio/fecha.

Esta estructura permite:
- Calcular precios promedio.
- Analizar dispersión de precios.
- Realizar comparaciones entre establecimientos.

---

### 4.2 Archivo `basket.json` – Canasta básica

El archivo define los **productos básicos** y su consumo mensual recomendado, expresado en **"u/kg/lt"**.

#### Justificación

- Sirve como referencia normativa.
- Permite evaluar si el salario cubre las necesidades mínimas.
- No depende de precios, solo de cantidades.

Este archivo es clave para vincular el análisis económico con una noción de necesidad básica.

---

### 4.3 Archivo `salaries.json` – Salarios por categoría laboral

Contiene los salarios mensuales organizados por categorías laborales oficiales.

#### Campos

- Categoría laboral.
- Salario mensual en CUP.
- Horas laborales semanales.

Se utiliza el **salario promedio**, como valor representativo del ingreso del trabajador.

---

## 5. Estructuras

### 5.1 Módulos

Las funciones del proyecto se encuentra organizado en archivos `.py`, dentro de la carpeta `modules`.

### 5.2 Archivo `normalize.py` - Procesamiento de datos

Función:
Constituye la **funcionalidad** del proyecto, siendo responsable de la **lectura, estructura, agregación y análisis** de la información de los archivos `JSON`. Su función es **transformar datos crudos a datos cuantitativos**, que se utilizan para evaluar costos, salarios, y capacidad adquisitiva.

### 5.3 Archivo `tools.py` - Construcción de la canasta

Función:
Su propósito es **reducir la variabilidad de los datos** (gramajes) y construir la **canasta**, basada en valores dominantes.

### 5.4 Archivo `charts.py` - Visualización

Función:
Transforma los **indicadores numéricos** obtenido tras normalizar en **representaciones visuales**, coherentes de acuerdo al **storytelling**

---

### 5.2 Notebook: `story.ipynb`

- Importar funciones.
- Ejecutar el análisis.
- Construir el storytelling.
- Integrar texto, gráficos y resultados.

---

## 6. Resultados obtenidos

A partir del análisis realizado, se obtuvieron los siguientes resultados principales:

- Existe una **alta variabilidad de precios** para un mismo producto entre distintas MiPymes.
- El salario promedio permite adquirir grandes cantidades de algunos productos, pero resulta claramente insuficiente para otros.
- En varios casos, un solo producto requiere **uno o más días completos de trabajo** para ser adquirido.
- La capacidad de cubrir el consumo mensual recomendado no está garantizada para todos los productos.

Los resultados se presentan de forma progresiva mediante visualizaciones integradas en `story.ipynb`.

---

## 7. Discusión

Los resultados muestran que el problema es que el **salario promedio** no está acorde a los precios de la **canasta básica**.

---

## 8. Conclusiones

El análisis evidencia que, bajo las condiciones actuales, el salario promedio del trabajador cubano presenta serias limitaciones para garantizar el acceso pleno a los productos básicos comercializados por MiPymes.

Este proyecto demuestra cómo, a partir de datos estructurados y herramientas simples, es posible analizar problemáticas económicas reales de alto impacto social.

---

## 9. Instrucciones

Pasos:
- Abrir el archivo `story.ipynb`.
- Ejecutar todas las celdas.

Requisitos:
- Python 3x.
- Instalar biblioteca: `pip install matplotlib`.

---

## 10. Consideraciones finales

Este informe complementa a `story.ipynb` y cumple con los requisitos académicos establecidos para el proyecto de Ciencia de Datos.

El trabajo no pretende emitir juicios normativos, sino ofrecer una lectura cuantitativa fundamentada en datos reales y reproducibles.

---