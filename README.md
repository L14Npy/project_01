# Precios en tiempos de cólera

## Descripción:
Este proyecto analiza la capacidad del trabajador cubano para adquirir productos básicos de la canasta alimentaria, utilizando datos de MiPymes, salarios y gramajes de consumo.

## Fuentes de Datos
1. **MiPymes:** 30 MiPymes analizadas con al menos 10 productos (alimentos). Se registraron precios históricos y características de cada producto.
2. **Canasta básica:** Documento JSON con gramaje de cada producto.
3. **Salarios:** Lista de salarios por categoría laboral, extraída de fuentes oficiales.

## Estructura del Repositorio
- `notebook.ipynb` : Jupyter Notebook con la historia basada en datos.
- `functions.py` : Biblioteca de funciones implementadas para el proyecto.
- `data/` : Carpeta que contiene los archivos de datos utilizados.
  - `pymes.json` : Datos de precios y productos de las MiPymes.
  - `basket.json` : Gramajes de productos.
  - `salaries.json` : Información de salarios.

## Gráficas del Proyecto
1. **Precio promedio por producto**: Permite identificar jerarquía de precios y establecer referencia inicial.
2. **Distribución de precios**: Visualiza la variabilidad de precios entre MiPymes.
3. **Salario promedio vs productos**: Introduce la restricción económica del salario y su relación con cada producto.
4. **Porcentaje del salario por producto**: Indica la fracción del ingreso que requiere cada producto.
5. **Días de laborales necesarios**: Muestra el esfuerzo laboral requerido para adquirir cada producto, traduciendo precios a tiempo de trabajo.

## Funcionalidades Implementadas
- Cálculo de precio promedio de productos.
- Extracción de listas y normalización de precios.
- Cálculo del costo de la canasta por producto.
- Comparación con salario promedio.
- Transformación de precios a porcentaje del salario y días de trabajo.

## Instrucciones de Uso
1. Clonar el repositorio.
2. Abrir `story.ipynb` en Jupyter Notebook.
3. Asegurarse de que los archivos de datos estén en la carpeta `data/`.
4. Ejecutar las celdas de código para reproducir las gráficas y análisis.

## Requisitos
- Python 3.x
- Biblioteca permitida para gráficas: matplotlib
- No se utilizaron bibliotecas externas.

## Conclusión
El proyecto evidencia que el salario promedio cubano limita severamente la capacidad de adquirir productos esenciales, y que algunos bienes requieren varios días de trabajo para ser adquiridos.

---

* **Autor:** L14N
* **Fecha:** 2025-12-31