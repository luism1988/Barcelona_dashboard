import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

from data.get_data import get_all, get_district_coordinates , get_neighborhood_coordinates
from data.graph import  map_plot, bar_plot
from streamlit_folium import folium_static
from  funtions import df_format_fixer, get_coordenates,convert_df
import matplotlib.pyplot as plt
import seaborn as sns


with st.sidebar:
    sidebar_selection = st.radio('Select one:', ["Population and location by District","Population and location by Neighborhood" ,"Transports","About"])
if sidebar_selection == "Population and location by District":

    st.title('BARCELONA DASHBOARD')
    st.image('./barcelona_5.png')

    year = st.slider('Pick a number', 2013, 2017)
    #selection = st.selectbox('Pick one', ["Select","District", "Neighborhood"])

    df = pd.DataFrame(get_all(year))
    df_format = df_format_fixer(df)

    #if selection == "District":
    st.text("A continuación puedes ver la población de los diferentes distritos de Barcelona y su ubicacion en el mapa")
    stratify = st.radio('Pick a stratify', [None,'Gender', 'Age'])
        
    fig= bar_plot(df_format,a="District",b="Population",c=stratify)
    plt.savefig("District.png")
    st.pyplot(fig)
    
    st.download_button('Download data', convert_df(df_format),file_name="District_data.csv")
    with open("District.png", "rb") as file:
        btn = st.download_button(
        label="Download graph",
        data=file,
        file_name="District.png",
        )

           
    coordinates_dict= get_district_coordinates()
    map_district = map_plot(get_coordenates(coordinates_dict))
    folium_static(map_district)






      
if sidebar_selection =="Population and location by Neighborhood":
    year = st.slider('Pick a number', 2013, 2017)                          
    df = pd.DataFrame(get_all(year))
    selection2 = st.selectbox('Elige distrito',['Ciutat Vella', 'Eixample', 'Sants-Montjuïc', 'Les Corts',
    'Sarrià-Sant Gervasi', 'Gràcia', 'Horta-Guinardó', 'Nou Barris',
    'Sant Andreu', 'Sant Martí'] )
    st.text("A continuación puedes ver la población de los diferentes Barrios de Barcelona y su ubicacion en el mapa")
    stratify = st.radio('Pick a stratify', [None,'Gender', 'Age'])
    df_format = df_format_fixer(df)
    df_format_selection= df_format[df_format['District']==selection2]
        
    fig = bar_plot(df_format_selection,a="Neighborhood",b="Population",c=stratify)
    plt.savefig("Neighborhood.png")
    st.pyplot(fig)
    

    st.download_button('Download Neighborhood data', convert_df(df_format),file_name="Neighborhood.csv")
    with open("Neighborhood.png", "rb") as file:
        btn = st.download_button(
        label="Download graph",
        data=file,
        file_name="Neighborhood.png",
        )



    get_coordinates_neighborhood= get_neighborhood_coordinates()
    match_coordinates_neighborhood = []
    coordinates_neighborhood = get_coordenates(get_coordinates_neighborhood)
    for i in coordinates_neighborhood:
        if i["Name"] in list(list(df_format_selection["Neighborhood"].unique())):
            match_coordinates_neighborhood.append(i)
    map_neighborhood = map_plot(match_coordinates_neighborhood)
    folium_static(map_neighborhood)




        
if sidebar_selection == "Transports":
    st.title('BARCELONA DASHBOARD')
    st.image('./barcelona_5.png')
    st.text("En construcción")

if sidebar_selection == "About":
    st.title('BARCELONA DASHBOARD')
    st.image('./barcelona_5.png')
    st.text("En construcción")
    


