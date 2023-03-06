import streamlit as st
import pandas as pd
from fpdf import FPDF


from data.get_data import get_all, get_district_coordinates , get_neighborhood_coordinates
from data.graph import  map_plot, bar_plot
from data.funtions import df_format_fixer, get_coordenates, convert_df
from streamlit_folium import folium_static


# create sidebar with four "pages": ["Population and location by District","Population and location by Neighborhood" ,"Transports","About"]
with st.sidebar:
    sidebar_selection = st.radio('Navigation', ["Population and location by District","Population and location by Neighborhood" ,"About"])#"Transports"

#page one: show Population and location by District
if sidebar_selection == "Population and location by District":

    #Title and header image 
    st.markdown("<h1 style='text-align: center; color: black;'>BARCELONA DASHBOARD</h1>", unsafe_allow_html=True)
    st.image('./img/barcelona_5.png')

    #slider for select data year
    year = st.slider('Select data year:', 2013, 2017)
    df = pd.DataFrame(get_all(year)) #function get_all get query from the API
    df_format = df_format_fixer(df) # the function "df_format_fixe"  transforms the data in the dataset to be plotted

    #description of the results
    st.text("Barcelona population by districts:")
    #slider for select variable to stratify
    stratify = st.radio('Stratify by:', [None,'Gender', 'Age'])
    
    #data plot
    fig= bar_plot(df_format,a="District",b="Population",c=stratify)
    st.pyplot(fig)
   
    
    #data download
    st.text("Download data and image:")
    df_download = df_format.groupby("District").sum().reset_index()
    st.download_button('Download district data', convert_df(df_download),file_name="District_data.csv")
   
    with open("picture.png", "rb") as file:
        btn = st.download_button(
        label="Download graph",
        data=file,
        file_name="District.png",
        )

    #map plot   
    st.text("Barcelona districts location:")    
    coordinates_dict= get_district_coordinates() #function get_district_coordinates(), get query coordinates from the API
    map_district = map_plot(get_coordenates(coordinates_dict)) #function get_coordinates()transforms the data to be plotted
    folium_static(map_district)

    #pdf report creator
    
    pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(25, 10, txt="BARCELONA DASHBOARD")
    pdf.set_font('Arial', 'B', 12)
    pdf.image('./img/barcelona_5.png',x=20, y=30, w=150, h=28)
    pdf.text(x=25, y=70,txt="Population and location by District")
    pdf.image('picture.png',x=20,y=75,w=100,h=100)
    pdf.set_font('Arial',"", 12)
    # Cambiar posición de la tabla
    pdf.set_xy(25, 190)
    # Agregar encabezado de la tabla
    pdf.cell(40, 10, 'District', 1) #variable
    pdf.cell(40, 10, 'Population', 1)
    pdf.ln()
    for index, row in df_download.iterrows():
        pdf.cell(40, 10, str(row['District']), 1)
        pdf.cell(40, 10, str(row['Population']), 1)
        pdf.ln()
    pdf.output("report.pdf")
    st.text("Download pdf report:")
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
    year = st.slider('Select data year:', 2013, 2017)  
    df = pd.DataFrame(get_all(year)) #function get_all get query from the API

    #selectbox for select a District, for then plot de population by Neighborhood
    selection2 = st.selectbox('Select district',['Ciutat Vella', 'Eixample', 'Sants-Montjuïc', 'Les Corts',
    'Sarrià-Sant Gervasi', 'Gràcia', 'Horta-Guinardó', 'Nou Barris',
    'Sant Andreu', 'Sant Martí'] )

    #description of the results
    st.text("Barcelona neighborhoods population by district:")
    
    #slider for select variable to stratify
    stratify = st.radio('Pick a stratify', [None,'Gender', 'Age'])
    
    #transforms the data in the dataset to be plotted
    df_format = df_format_fixer(df) 
    df_format_selection= df_format[df_format['District']==selection2]
    
    #data plot   
    fig = bar_plot(df_format_selection,a="Neighborhood",b="Population",c=stratify)
    st.pyplot(fig)
    
    #data download
    st.text("Download data and image:")
    df_download = df_format_selection.groupby("Neighborhood").sum().reset_index()
    st.download_button('Download neighborhood data', convert_df(df_download),file_name="Neighborhood.csv")
    with open("picture.png", "rb") as file:
        btn = st.download_button(
        label="Download graph",
        data=file,
        file_name="Neighborhood.png",
        )

    #map plot
    st.text("Barcelona neighborhoods location by District:")
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
    pdf.cell(25, 10, txt="BARCELONA DASHBOARD")
    pdf.set_font('Arial', 'B', 12)
    pdf.image('./img/barcelona_5.png',x=20, y=30, w=150, h=28)
    pdf.text(x=25, y=70,txt="Barcelona neighborhoods population by district:")
    pdf.image('picture.png',x=20,y=75,w=100,h=100)
    pdf.set_font('Arial',"", 12)
    # Cambiar posición de la tabla
    pdf.set_xy(25, 190)
    # Agregar encabezado de la tabla
    pdf.cell(40, 10, 'Neighborhood', 1)
    pdf.cell(40, 10, 'Population', 1)
    pdf.ln()
    for index, row in df_download.iterrows():
        pdf.cell(40, 10, str(row['Neighborhood']), 1)
        pdf.cell(40, 10, str(row['Population']), 1)
        pdf.ln()
    pdf.output("report.pdf")

    #pdf report download
    st.text("Download pdf report:")
    with open('report.pdf', "rb") as file2:
        btn = st.download_button(
        label='Download report',
        data = file2,
        file_name="repo.pdf",
        )
    




if sidebar_selection == "About":
    st.markdown("<h1 style='text-align: center; color: black;'>BARCELONA DASHBOARD</h1>", unsafe_allow_html=True)
    st.image('./img/barcelona_5.png')
    st.text("En construcción")
  