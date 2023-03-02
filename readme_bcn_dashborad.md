
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
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/1.png?raw=true" width="600">
</p>
     
1.2- Población y ubicación por distrito:

- 1.2.1- Punto “A”: En la parte superior podemos seleccionar el año de visualización.

- 1.2.2- Punto “B”: Podemos seleccionar la variable de es traficación (Ninguna, género o edad)

<p align="center">
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/db2.png?raw=true" width="400">
</p>

- 1.2.3- Grafico de población por distrito:

<p align="center">
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/db4.png?raw=true" width="400">
</p>

- 1.2.4- Grafico de población por distrito estratificado por genero:

<p align="center">
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/11.png?raw=true" width="400">
</p>

- 1.2.5- Grafico de población por distrito estratificado por edad:

<p align="center">
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/12.png?raw=true" width="400">
</p>

- 1.2.6- Grafico ubicación de los distritos:

<p align="center">
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/db6.png?raw=true" width="400">
</p>

- 1.2.7- Boton de descarga de los datos en formato csv:

<p align="center">
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/boton%20de%20descarga%20distritos.png?raw=true" width="100">
</p>

1.3- Población y ubicación por barrio:
- 1.3.1- Punto “A”: En la parte superior podemos seleccionar el año de visualización.

- 1.3.2- Punto “B”: Seleccionar el distrito para visualizar la población y ubicación de los barrios que componen a éste.

- 1.3.3- Punto “C”: Podemos seleccionar la variable de es traficación (Ninguna, género o edad).

<p align="center">
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/Sin%20t%C3%ADtulo.png?raw=true" width="300">
</p>

- 1.3.4- Grafico de población por barrios:

<p align="center">
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/Captura%20de%20pantalla%202023-03-02%20231321.png?raw=true" width="400">
</p>

- 1.3.5-Grafico ubicación de los barrios que conforman un distrito:

<p align="center">
  <img src="-" width="400">
</p>

- 1.3.6-Boton de descarga de los datos en formato csv:

<p align="center">
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/boton%20de%20descarga%20barrios.png?raw=true" width="150">
</p>

