
import matplotlib.pyplot as plt
import folium
import seaborn as sns


def bar_plot(df,a:str,b:str,c= None): 
    plt.figure(figsize=(6,6))
    fig, ax = plt.subplots(figsize=(5,5))
    sns.barplot(data=df, x = a ,y = b, hue=c, estimator=sum) 
    plt.xticks(rotation=70)
    plt.ylabel('Population')
    plt.tight_layout()
    fig.savefig("picture.png",pad_inches=0.5)
    return fig
    
def map_plot(dic):
    m = folium.Map(location=[41.40879, 2.2], zoom_start=11.5)
    for dist in dic:
        folium.Marker(location= dist["coordinates"], tooltip=dist["Name"]).add_to(m)
    return m 






