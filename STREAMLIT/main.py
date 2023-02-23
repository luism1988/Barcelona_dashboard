import streamlit as st
import streamlit.components.v1 as components
import pandas as pd


from data.get_data import get_district, get_district_coordinates
from data.graph import bar_plot, district_map
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
import seaborn as sns
st.title('BARCELONA DASHBOARD')
st.image('./barcelona_5.png')

year = 2017
district_population = get_district(year)
df = pd.DataFrame(district_population[0])

plt.figure(figsize=(15,6))
fig, ax = plt.subplots()
sns.countplot(data=df, x='District.Name',hue="Year") # tambien se puede estratificar por genero hue="Gender"
plt.xticks(rotation=45)
st.pyplot(fig)

"""# inicio barplot por matplolit
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
graph= bar_plot(x,y)
st.pyplot(graph)
# fin barplot por matplolit
"""

#coordinates_dict = get_district_coordinates()

coordinates_dict =[
{"Name":"Ciutat Vella","coordinates": [41.38022, 2.17319]},
{"Name":"Sants-Montjuïc","coordinates": [41.37263, 2.1546]},
{"Name":"Eixample","coordinates": [41.38896, 2.16179]},
{"Name":"Les Corts","coordinates": [41.38845,2.12171]},
{"Name":"Sarrià-Sant Gervasi","coordinates": [41.40237, 2.15641]},
{"Name":"Gràcia","coordinates": [41.40237, 2.15641]},
{"Name":"Horta-Guinardó","coordinates": [41.41849, 2.1677]},
{"Name":"Nou Barris","coordinates": [41.44163, 2.17727]},
{"Name":"Sant Andreu","coordinates": [41.43541, 2.18982]},
{"Name":"Sant Martí","coordinates": [41.41814, 2.19933]}
]
map_district = district_map(coordinates_dict)
folium_static(map_district)
