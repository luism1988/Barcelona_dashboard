import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

from data.get_data import get_district, get_district_coordinates ,get_neighborhood, get_neighborhood_coordinates
from data.graph import  map_plot, bar_plot
from streamlit_folium import folium_static
from  funtions import df_format_fixer, get_coordenates,convert_df
import matplotlib.pyplot as plt
import seaborn


with st.sidebar:
    sidebar_selection = st.radio('Select one:', ["Population by District or Neighborhood","Location by District or Neighborhood" ,"Statistics","About"])
if sidebar_selection == "Population by District or Neighborhood":

    st.title('BARCELONA DASHBOARD')
    st.image('./barcelona_5.png')

    year = st.slider('Pick a number', 2013, 2017)
    selection = st.selectbox('Pick one', ["Select","District", "Neighborhood"])

    if selection == "District":
        st.text("A continuación puedes ver la población de los diferentes distritos de Barcelona y su ubicacion en el mapa")
        df = pd.DataFrame(get_district(year))
        df_format = df_format_fixer(df)
        df_to_plot = df_format.groupby("District").sum().reset_index().sort_values('Population',ascending=False)
        fig= bar_plot(df_to_plot,a="District")
        plt.savefig("District.png")
        st.pyplot(fig)
        
        st.download_button('Download data', convert_df(df_to_plot),file_name="District_data.csv")
        with open("District.png", "rb") as file:
            btn = st.download_button(
            label="Download graph",
            data=file,
            file_name="District.png",
          )

      
        


             
    if selection == "Neighborhood":
        df = pd.DataFrame(get_neighborhood(year))
        selection2 = st.selectbox('Elige distrito',['Ciutat Vella', 'Eixample', 'Sants-Montjuïc', 'Les Corts',
       'Sarrià-Sant Gervasi', 'Gràcia', 'Horta-Guinardó', 'Nou Barris',
       'Sant Andreu', 'Sant Martí'] )
        st.text("A continuación puedes ver la población de los diferentes Barrios de Barcelona y su ubicacion en el mapa")

        df_format = df_format_fixer(df)
        df_format_selection= df_format[df_format['District']==selection2]
        df_to_plot = df_format_selection.groupby("Neighborhood").sum().reset_index().sort_values('Population',ascending=False)


        fig= bar_plot(df_to_plot,a="Neighborhood")
        plt.savefig("Neighborhood.png")

        st.pyplot(fig)
        st.download_button('Download Neighborhood data', convert_df(df_to_plot),file_name="Neighborhood.csv")
        with open("Neighborhood.png", "rb") as file:
            btn = st.download_button(
            label="Download graph",
            data=file,
            file_name="Neighborhood.png",
          )
      


        
if sidebar_selection == "Location by District or Neighborhood":
    selection_location = st.selectbox('Pick one', ["Select","District", "Neighborhood"])
    if selection_location == "District":
        coordinates_dict= get_district_coordinates()
        map_district = map_plot(get_coordenates(coordinates_dict))
        folium_static(map_district)

    if selection_location == "Neighborhood":
        coordinates_neighborhood= get_neighborhood_coordinates()
        map_neighborhood = map_plot(get_coordenates(coordinates_neighborhood))
        folium_static(map_neighborhood)

