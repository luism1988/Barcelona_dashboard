import pandas as pd
import streamlit as st
from fpdf import FPDF

def df_format_fixer(df):
    distritos = []
    barrios = []
    poblacion = []
    genero = []
    edad = []
    columns = ["District","Neighborhood","Population","Gender","Age"]
    for i in df["Number"]:
        poblacion.append(int(i))
    for i in df["District"]: 
        distritos.append(i["Name"])
    for i in df[str("Neighborhood")]: 
        barrios.append(i["Name"])
    for i in df["Gender"]: 
        genero.append(i)
    for i in df["Age"]:
        if i in ['0-4', '5-9', '10-14', '15-19']:
            edad.append('0-19')
        elif i in ['20-24', '25-29', '30-34', '35-39','40-44']:
            edad.append('20-44')
        elif i in ['45-49', '50-54', '55-59', '60-64']:
            edad.append('45-64')
        elif i in ['65-69', '70-74','75-79', '80-84', '85-89', '90-94', '>=95']:
            edad.append('65->=95')
    df_fixed = pd.DataFrame(list(zip(distritos,barrios,poblacion,genero,edad)),columns=columns)
    return df_fixed

def get_coordenates(list):
    res = []
    for i in list:
        res.append({"Name":i["Name"],"coordinates": [i["latitude"], i["Longitude"]]})
    return res

@st.cache_data
def convert_df(df):
    return df.to_csv().encode('utf-8') 

def pdf_creator_district(img,df):

    pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(25, 10, txt="BARCELONA DASHBOARD")
    pdf.set_font('Arial', 'B', 12)
    pdf.image('./img/barcelona_5.png',x=20, y=30, w=150, h=28)
    pdf.text(x=25, y=70,txt="Barcelona population by districts:")
    pdf.image(img,x=20,y=75,w=100,h=100)
    pdf.set_font('Arial',"", 12)
    # Cambiar posición de la tabla
    pdf.set_xy(25, 190)
    # Agregar encabezado de la tabla
    pdf.cell(40, 10, 'District', 1)
    pdf.cell(40, 10, 'Population', 1)
    pdf.ln()
    for index, row in df.iterrows():
        pdf.cell(40, 10, str(row['District']), 1)
        pdf.cell(40, 10, str(row['Population']), 1)
        pdf.ln()

def pdf_creator_neighborhood(img,df):

    pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(25, 10, txt="BARCELONA DASHBOARD")
    pdf.set_font('Arial', 'B', 12)
    pdf.image('./img/barcelona_5.png',x=20, y=30, w=150, h=28)
    pdf.text(x=25, y=70,txt="Barcelona neighborhoods population by district:")
    pdf.image(img,x=20,y=75,w=100,h=100)
    pdf.set_font('Arial',"", 12)
    # Cambiar posición de la tabla
    pdf.set_xy(25, 190)
    # Agregar encabezado de la tabla
    pdf.cell(40, 10, 'Neighborhood', 1)
    pdf.cell(40, 10, 'Population', 1)
    pdf.ln()
    for index, row in df.iterrows():
        pdf.cell(40, 10, str(row['Neighborhood']), 1)
        pdf.cell(40, 10, str(row['Population']), 1)
        pdf.ln()


