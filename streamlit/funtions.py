import pandas as pd

def df_format_fixer(df):
    distritos = []
    poblacion = []
    Gender = []
    columns = ["District","Population","Gender"]
    for i in df["Number"]:
        poblacion.append(int(i))
    for i in df["District"]: 
        distritos.append(i["Name"])
    for i in df["Gender"]: 
        Gender.append(i)
    df_fixed = pd.DataFrame(list(zip(distritos,poblacion,Gender)),columns=columns)
    return df_fixed