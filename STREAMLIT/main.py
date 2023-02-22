import streamlit as st
import streamlit.components.v1 as components
from data.get_data import get_district
from data.graph import bar_plot


st.title('BARCELONA DASHBOARD')
st.image('./barcelona_5.png')

year = 2017
district_population = get_district(year)

district_dict = {}
for element in district_population:
    if not element["District"]["Name"] in district_dict.keys():
        district_dict[element["District"]["Name"]] =int(element["Number"])
    else:
        a =district_dict[element["District"]["Name"]]
        district_dict[element["District"]["Name"]] += int(element["Number"])
x = []
y = []

for element in district_dict:
    x.append(element)
    y.append(district_dict[element])

print(x,y)

graph= bar_plot(x,y)

st.pyplot(graph)