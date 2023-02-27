#import plotly.io as pio
#import plotly.graph_objs as go
#import plotly_express as px
import matplotlib.pyplot as plt
import folium
import seaborn as sns


def count_plot(df): #Nota: esta funcion no la he probado, la cree en el avion.
    plt.figure(figsize=(20,6))
    fig, ax = plt.subplots()
    
    sns.barplot(data=df, x='District',y = 'Population',) # tambien se puede estratificar por genero hue="Gender"
    plt.xticks(rotation=70)
    plt.ylabel('Population')
    return fig
    

def district_map(dic):
    m = folium.Map(location=[41.38879, 2.15899], zoom_start=11.5)
    for dist in dic:
        folium.Marker(location= dist["coordinates"], tooltip=dist["Name"]).add_to(m)
    return m 






