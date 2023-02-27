import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

from data.get_data import get_district, get_district_coordinates
from data.graph import  district_map, count_plot
from streamlit_folium import folium_static
from  funtions import df_format_fixer
import matplotlib.pyplot as plt
import seaborn


with st.sidebar:
    sidebar_selection = st.radio('Select one:', ["Population", "Statistics"])
if sidebar_selection == "Population":

    st.title('BARCELONA DASHBOARD')
    st.image('./barcelona_5.png')


    selection = st.selectbox('Pick one', ["-","District", "Neighborhood"])


    if selection == "District":
        st.text("A continuación puedes ver la población de los diferentes distritos de Barcelona y su ubicacion en el mapa")
        year = 2017
        df = pd.DataFrame(get_district(year))
        df_format = df_format_fixer(df)
        fig= count_plot(df_format.groupby("District").sum().reset_index().sort_values('Population',ascending=False,))
        st.pyplot(fig) 

        coordinates_dict =[
        {"Name":"Ciutat Vella","coordinates": [41.38022, 2.17319]},
        {"Name":"Sants-Montjuïc","coordinates": [41.37263, 2.1546]},
        {"Name":"Eixample","coordinates": [41.38896, 2.16179]},
        {"Name":"Les Corts","coordinates": [41.38845,2.12171]},
        {"Name":"Sarrià-Sant Gervasi","coordinates": [41.40237, 2.15641]},
        {"Name":"Gràcia","coordinates": [41.40237, 2.15641]},
        {"Name":"Horta-Guinardó","coordinates": [41.41849, 2.1677]},
        {"Name":"Nou Barris","coordinates": [41.44163, 2.17727]},
        {"Name":"Sant Andreu","coordinates": [41.43541, 2.18982]},
        {"Name":"Sant Martí","coordinates": [41.41814, 2.19933]}
        ]
        map_district = district_map(coordinates_dict)
        folium_static(map_district)
    #if selection == "Neighborhood":
