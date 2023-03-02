
# Barcelona_Dashboard

## Descripción y objetivo:
Barcelona Dashboard es un proyecto académico con el cual podemos visualizar a través de diagramas de barras, la población de Barcelona en sus diferentes distritos y barrios. También, podemos estratificar la población por el año del padrón municipal, género y edad de los habitantes. Y visualizar en el mapa la ubicación de distritos y barrios.

El dataset ha sido descargado de: https://www.kaggle.com/datasets/xvivancos/barcelona-data-sets

En su desarrollo se emplearon diferentes stacks tecnológicos como Python, Pandas, FastAPI, MongoDB y Streamlit (entre otros).

### Los pasos para realizar este proyecto fueron:
- 1 Selección del dataset de Barcelona entre varias opciones.
- 2 Exploración del dataset y tratamiento de datos duplicados y nulos.
- 3 Carga del dataset en MongoDB Atlas.
- 4 Creación de la API:
    - Conexión con MongoDB.
    - Creación de la Main.
    - Creación/definición de los routers y endpoints.
- 5 Creación del Streamlit:
    - Conexión con la API
    - Creación y parametrización de las visualizaciones.


### 1-Descripción del Dashboard

1.1 -Navegación:
    En la barra lateral podemos seleccionar entre visualizar la población y ubicación por distrito.


<p align="center">
  <img src="https://raw.githubusercontent.com/luism1988/Barcelona_dashboard/main/img_readme/db1.png?token=GHSAT0AAAAAAB5ILY6AOKUSCYCSKQ2SAFPEZAA6S3Q" width="400">
</p>
     
1.2- Población y ubicación por distrito:

- 1.2.1- Punto “A”: En la parte superior podemos seleccionar el año de visualización.

- 1.2.2- Punto “B”: Podemos seleccionar la variable de es traficación (Ninguna, género o edad)

- 1.2.3- Grafico de población por distrito:

- 1.2.4- Grafico de población por distrito estratificado por genero:

- 1.2.5- Grafico de población por distrito estratificado por edad:

- 1.2.6- Grafico ubicación de los distritos:

- 1.2.7- Boton de descarga de los datos en formato csv:

1.3- Población y ubicación por barrio:
- 1.3.1- Punto “A”: En la parte superior podemos seleccionar el año de visualización.

- 1.3.2- Punto “B”: Seleccionar el distrito para visualizar la población y ubicación de los barrios que componen a éste.

- 1.3.3- Punto “C”: Podemos seleccionar la variable de es traficación (Ninguna, género o edad).

- 1.3.4- Grafico de población por barrios:

- 1.3.5-Grafico ubicación de los barrios que conforman un distrito:

- 1.3.6-Boton de descarga de los datos en formato csv:

