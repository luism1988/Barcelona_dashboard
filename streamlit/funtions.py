import pandas as pd

def df_format_fixer(df,string:str):
    distritos = []
    poblacion = []
    Gender = []
    columns = [string,"Population","Gender"]
    for i in df["Number"]:
        poblacion.append(int(i))
    for i in df[str(string)]: 
        distritos.append(i["Name"])
    for i in df["Gender"]: 
        Gender.append(i)
    df_fixed = pd.DataFrame(list(zip(distritos,poblacion,Gender)),columns=columns)
    return df_fixed

def get_coordenates(list):
    res = []
    for i in list:
        res.append({"Name":i["Name"],"coordinates": [i["latitude"], i["Longitude"]]})
    return res