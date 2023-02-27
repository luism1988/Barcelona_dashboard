import pandas as pd
import streamlit as st

def df_format_fixer(df):
    distritos = []
    barrios = []
    poblacion = []
    Gender = []
    columns = ["District","Neighborhood","Population","Gender"]
    for i in df["Number"]:
        poblacion.append(int(i))
    for i in df["District"]: 
        distritos.append(i["Name"])
    for i in df[str("Neighborhood")]: 
        barrios.append(i["Name"])
    for i in df["Gender"]: 
        Gender.append(i)
    df_fixed = pd.DataFrame(list(zip(distritos,barrios,poblacion,Gender)),columns=columns)
    return df_fixed

def get_coordenates(list):
    res = []
    for i in list:
        res.append({"Name":i["Name"],"coordinates": [i["latitude"], i["Longitude"]]})
    return res
@st.cache_data
def convert_df(df):
    return df.to_csv().encode('utf-8') 