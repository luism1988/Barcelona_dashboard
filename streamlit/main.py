import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

from data.get_data import get_district, get_district_coordinates ,get_neighborhood, get_neighborhood_coordinates
from data.graph import  map_plot, bar_plot, bar_plot_Neighborhood
from streamlit_folium import folium_static
from  funtions import df_format_fixer, get_coordenates
import matplotlib.pyplot as plt
import seaborn


with st.sidebar:
    sidebar_selection = st.radio('Select one:', ["Population and location", "Statistics"])
if sidebar_selection == "Population and location":

    st.title('BARCELONA DASHBOARD')
    st.image('./barcelona_5.png')

    year = st.slider('Pick a number', 2013, 2017)
    selection = st.selectbox('Pick one', ["-","District", "Neighborhood"])

    if selection == "District":
        st.text("A continuación puedes ver la población de los diferentes distritos de Barcelona y su ubicacion en el mapa")
        df = pd.DataFrame(get_district(year))
        df_format = df_format_fixer(df,selection)
        fig= bar_plot(df_format.groupby("District").sum().reset_index().sort_values('Population',ascending=False),a="District")
        st.pyplot(fig) 

        coordinates_dict= get_district_coordinates()
        map_district = map_plot(get_coordenates(coordinates_dict))
        folium_static(map_district)

   
               
    if selection == "Neighborhood":
        st.text("A continuación puedes ver la población de los diferentes Barrios de Barcelona y su ubicacion en el mapa")
        df = pd.DataFrame(get_neighborhood(year))
        df_format = df_format_fixer(df,selection)
        fig= bar_plot_Neighborhood(df_format.groupby("Neighborhood").sum().reset_index().sort_values('Population',ascending=False),a="Neighborhood")
        st.pyplot(fig)

        coordinates_neighborhood= get_neighborhood_coordinates()
        map_neighborhood = map_plot(get_coordenates(coordinates_neighborhood))
        folium_static(map_neighborhood)