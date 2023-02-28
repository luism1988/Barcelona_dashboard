import pandas as pd
import streamlit as st

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