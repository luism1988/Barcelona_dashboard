#import plotly.io as pio
#import plotly.graph_objs as go
#import plotly_express as px
import matplotlib.pyplot as plt
import folium
import seaborn as sns
def bar_plot(df):
    plt.figure(figsize=(15,6))
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='District.Name',hue="Year") # tambien se puede estratificar por genero hue="Gender"
    plt.xticks(rotation=45)
    return fig


def count_plot(df): #Nota: esta funcion no la he probado, la cree en el avion.
    plt.figure(figsize=(15,6))
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='District.Name',hue="Year") # tambien se puede estratificar por genero hue="Gender"
    plt.xticks(rotation=45)
    return fig
    

"""def bar_plot(x,y):
    plt.figure(figsize=(15,6))
    fig, ax = plt.subplots()
    ax.bar(x, y)
    plt.xticks(rotation=75)
    return fig
"""
def district_map(dic):
    m = folium.Map(location=[41.38879, 2.15899], zoom_start=12)
    for dist in dic:
        folium.Marker(location= dist["coordinates"], tooltip=dist["Name"]).add_to(m)
    return m 






