<p align="center">
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/barcelona_5.png?raw=true" width="400">
</p>

# Barcelona Dashboard

## Description and objective:
Barcelona Dashboard is an academic project where we can visualize, through bar charts, Barcelona populatio by districts and neighborhoods. Also, we can stratify the population by the year of the municipal register, gender and age of the poblation. And visualize on the map the location of districts and neighborhoods.

The  dataset has been selected and downloaded from: [Open Data BCN](https://www.kaggle.com/xvivancos/barcelona-data-sets)

In the developing, different technological stacks were used like Python, Pandas, FastAPI, MongoDB and Streamlit (among others).

### The steps towards developing the project is:
- 1 Select Barcelona dataset.
- 2 Dataset exploration  and treatment of duplicate and null data.
- 3 Dataset load in MongoDB Atlas( Previously treatment).
- 4 -API creation (using FastAPI):
     - Connection with MongoDB.
     - Definition of routers and endpoints.
- 5 Streamlit creation:
     - API connection.
     - Creation and parameterization of visualizations.


### 1-Dashboard description

1.1 -Navigation:
        At sidebar you can select between seeing the population and location by district or neighborhood.

<p align="center">
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/1.png?raw=true" width="600">
</p>
     
1.2- Population and location by district:

- 1.2.1- A: you can select the year of display.

- 1.2.2- B: you can select the stratification variable (None, gender or age)

<p align="center">
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/db2.png?raw=true" width="400">
</p>

- 1.2.3- Population graph by district:

<p align="center">
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/db4.png?raw=true" width="400">
</p>

- 1.2.4- District population stratified by gender:

<p align="center">
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/11.png?raw=true" width="400">
</p>

- 1.2.5- District population stratified by age:

<p align="center">
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/12.png?raw=true" width="400">
</p>

- 1.2.6- Districts location graph:

<p align="center">
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/db6.png?raw=true" width="400">
</p>

- 1.2.7- Data download button (.csv):

<p align="center">
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/boton%20de%20descarga%20distritos.png?raw=true" width="100">
</p>

1.3- Population and location by neighborhood:
- 1.3.1- A: you can select the year of display.

- 1.3.2- B: Select a district to view the population and location of the neighborhoods that make up it.

- 1.3.3- C: you can select the stratification variable (None, gender or age).

<p align="center">
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/Sin%20t%C3%ADtulo.png?raw=true" width="300">
</p>

- 1.3.4- Population graph by neighborhood:

<p align="center">
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/Captura%20de%20pantalla%202023-03-02%20231321.png?raw=true" width="400">
</p>

- 1.3.5-Neighborhood location graph:

<p align="center">
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/14.png?raw=true" width="400">
</p>

- 1.3.6-Data download button (.csv):

<p align="center">
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/boton%20de%20descarga%20barrios.png?raw=true" width="150">
</p>

### 2-Data flow:
<p align="center">
  <img src="https://github.com/luism1988/Barcelona_dashboard/blob/main/img_readme/flujo.png?raw=true" width="600">
</p>


