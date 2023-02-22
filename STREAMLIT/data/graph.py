#import plotly.io as pio
#import plotly.graph_objs as go
#import plotly_express as px
import matplotlib.pyplot as plt

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




