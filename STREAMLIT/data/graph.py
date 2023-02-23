#import plotly.io as pio
#import plotly.graph_objs as go
#import plotly_express as px
import matplotlib.pyplot as plt
import folium


#def bar_plot(x,y):
#    plt.figure(figsize=(12,6))
#    plt.bar(x, y)
#    plt.show()
def bar_plot(x,y):
    plt.figure(figsize=(15,6))
    fig, ax = plt.subplots()
    ax.bar(x, y)
    plt.xticks(rotation=75)
    return fig

def district_map(dic:dict):
    m = folium.Map(location=[41.38879, 2.15899], zoom_start=12)
    for dist in dict:
        folium.Marker(location= [dist["coordinates"][0],dist["coordinates"][0]], tooltip=dist["Name"]).add_to(m)
    return m 






