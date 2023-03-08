import streamlit as st
import pandas as pd
from fpdf import FPDF

from data.get_data import get_all, get_district_coordinates , get_neighborhood_coordinates
from data.graph import  map_plot, bar_plot
from data.funtions import df_format_fixer, get_coordenates, convert_df
from streamlit_folium import folium_static


# create sidebar with two "pages": ["Population and location by District","Population and location by Neighborhood"]
with st.sidebar:
    sidebar_selection = st.radio('Navigation', ["Home page","Population and location by District","Population and location by Neighborhood"])

if sidebar_selection == "Home page":
    #Title and header image 
    st.markdown("<h1 style='text-align: center; color: black;'>BARCELONA DASHBOARD</h1>", unsafe_allow_html=True)
    st.image('./img/barcelona_5.png')
    st.markdown("Barcelona Dashboard is an academic project where we can visualize, through bar charts, Barcelona populatio by districts and neighborhoods. Also, we can stratify the population by the year of the municipal register, gender and age of the poblation. And visualize on the map the location of districts and neighborhoods.")
    st.markdown("The dataset has been selected and downloaded from: [Open Data BCN](https://www.kaggle.com/xvivancos/barcelona-data-sets)")
    st.markdown("In the developing, different technological stacks were used like Python, Pandas, FastAPI, MongoDB and Streamlit (among others).")
    st.image('./img/home_page.png')
    #st.markdown("The steps towards developing the project were:")
    #st.markdown("1- Select Barcelona dataset.")
    #st.markdown("2- Dataset exploration  and treatment of duplicate and null data.")
    #st.markdown("3- Dataset load in MongoDB Atlas( Previously treatment).")
    #st.markdown("4-API creation (using FastAPI):")
    #st.markdown("-Connection with MongoDB.")
    #st.markdown("-Definition of routers and endpoints.")
    #st.markdown("5- Streamlit creation:")
    #st.markdown("-API connection.")
    #st.markdown("-Creation and setup of visualizations.")
    st.subheader("**Created by:**")
    st.subheader("Luis Manuel Rodríguez")
    st.markdown("**Data Analyst | Six Sigma Black Belt | Process Engineer**")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/luis-manuel-rodríguez-román-9b19a8bb)")
    st.markdown("[Github](https://github.com/luism1988)")
  

#page one: show Population and location by District
if sidebar_selection == "Population and location by District":

    #Title and header image 
    st.markdown("<h1 style='text-align: center; color: black;'>BARCELONA DASHBOARD</h1>", unsafe_allow_html=True)
    st.image('./img/barcelona_5.png')

    #slider for select data year
    year = st.slider('**Select data year:**', 2013, 2017)
    df = pd.DataFrame(get_all(year)) #function get_all get query from the API
    df_format = df_format_fixer(df) # the function "df_format_fixe"  transforms the data in the dataset to be plotted

    #description of the results
    st.markdown("**Barcelona population by districts:**")
    #slider for select variable to stratify
    stratify = st.radio('**Stratify by:**', [None,'Gender', 'Age'])
    
    #data plot
   
    fig= bar_plot(df_format,a="District",b="Population",c=stratify)
    st.pyplot(fig)

    #data download
    df_download = df_format.groupby("District").sum().reset_index()
    columns = st.columns(2)
    with columns[0]:
        st.markdown("**Download data:**")
        st.download_button('Download district data', convert_df(df_download),file_name="District_data.csv")
    with columns[1]:
        st.markdown("**Download image:**")
        with open("picture.png", "rb") as file:
            btn = st.download_button(
            label="Download graph",
            data=file,
            file_name="District.png",
            )
    

    
    

    #map plot   
    st.markdown("**Barcelona districts location:**")    
    coordinates_dict= get_district_coordinates() #function get_district_coordinates(), get query coordinates from the API
    map_district = map_plot(get_coordenates(coordinates_dict)) #function get_coordinates()transforms the data to be plotted
    folium_static(map_district)

    #pdf report creator
    
    pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(10, 10, txt="BARCELONA DASHBOARD")
    pdf.set_font('Arial', 'B', 12)
    pdf.image('./img/barcelona_5.png',x=20, y=30, w=150, h=28)
    pdf.text(x=10, y=70,txt="Population and location by District")
    pdf.image('picture.png',x=20,y=75,w=100,h=100)
    
    # Cambiar posición de la tabla
    
    pdf.text(x=10, y=180,txt="Population and location data by District")
    pdf.set_font('Arial',"", 12)
    pdf.set_xy(10, 190)
    # Agregar encabezado de la tabla
    pdf.cell(40, 6, 'District', 1) #variable
    pdf.cell(40, 6, 'Population', 1)
    pdf.ln()
    for index, row in df_download.iterrows():
        pdf.cell(40, 6, str(row['District']), 1)
        pdf.cell(40, 6, str(row['Population']), 1)
        pdf.ln()
    pdf.output("report.pdf")
    st.markdown("**Download pdf report:**")
    #pdf report download
    with open('report.pdf', "rb") as file2:
        btn = st.download_button(
        label='Download report',
        data = file2,
        file_name="repo.pdf",
        )
    
#page two: show Population and location by Neighborhood      
if sidebar_selection =="Population and location by Neighborhood":
    #Title and header image 
    st.markdown("<h1 style='text-align: center; color: black;'>BARCELONA DASHBOARD</h1>", unsafe_allow_html=True)
    st.image('./img/barcelona_5.png')

    #slider for select data year
    year = st.slider('**Select data year:**', 2013, 2017)  
    df = pd.DataFrame(get_all(year)) #function get_all get query from the API

    #selectbox for select a District, for then plot de population by Neighborhood
    selection2 = st.selectbox('**Select district**',['Ciutat Vella', 'Eixample', 'Sants-Montjuïc', 'Les Corts',
    'Sarrià-Sant Gervasi', 'Gràcia', 'Horta-Guinardó', 'Nou Barris',
    'Sant Andreu', 'Sant Martí'] )

    #description of the results
    st.markdown("**Barcelona neighborhoods population by district:**")
    
    #slider for select variable to stratify
    stratify = st.radio('Pick a stratify', [None,'Gender', 'Age'])
    
    #transforms the data in the dataset to be plotted
    df_format = df_format_fixer(df) 
    df_format_selection= df_format[df_format['District']==selection2]
    df_format_selection =df_format_selection.sort_values("District")
    
    #data plot   
    fig = bar_plot(df_format_selection,a="Neighborhood",b="Population",c=stratify)
    st.pyplot(fig)
    
    #data download
    df_download = df_format_selection.groupby("Neighborhood").sum().reset_index()
    columns = st.columns(2)
    with columns[0]:
        st.markdown("**Download data:**")
        st.download_button('Download neighborhood data', convert_df(df_download),file_name="Neighborhood.csv")
    with columns[1]:
        st.markdown("**Download image:**")
        with open("picture.png", "rb") as file:
            btn = st.download_button(
            label="Download graph",
            data=file,
            file_name="Neighborhood.png",
            )

    #map plot
    st.markdown("**Barcelona neighborhoods location by District:**")
    get_coordinates_neighborhood= get_neighborhood_coordinates()
    
    # match neiborhood with select district
    match_coordinates_neighborhood = []
    coordinates_neighborhood = get_coordenates(get_coordinates_neighborhood)
    for i in coordinates_neighborhood:
        if i["Name"] in list(list(df_format_selection["Neighborhood"].unique())):
            match_coordinates_neighborhood.append(i)
    map_neighborhood = map_plot(match_coordinates_neighborhood)
    #plot
    folium_static(map_neighborhood)

    #pdf report creator
    pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(10, 10, txt="BARCELONA DASHBOARD")
    pdf.set_font('Arial', 'B', 12)
    pdf.image('./img/barcelona_5.png',x=20, y=30, w=150, h=28)
    pdf.text(x=10, y=70,txt="Barcelona neighborhoods population by district:")
    pdf.image('picture.png',x=20,y=75,w=100,h=100)
    
    # Cambiar posición de la tabla
    pdf.text(x=10, y=180,txt="Population and location data by District")
    pdf.set_xy(10, 190)
    pdf.set_font('Arial',"", 12)
    # Agregar encabezado de la tabla
    pdf.cell(90, 6, 'Neighborhood', 1)
    pdf.cell(90, 6, 'Population', 1)
    pdf.ln()
    for index, row in df_download.iterrows():
        pdf.cell(90, 6, str(row['Neighborhood']), 1)
        pdf.cell(90, 6, str(row['Population']), 1)
        pdf.ln()
    pdf.output("report.pdf")

    #pdf report download
    st.markdown("**Download pdf report:**")
    with open('report.pdf', "rb") as file2:
        btn = st.download_button(
        label='Download report',
        data = file2,
        file_name="repo.pdf",
        )
