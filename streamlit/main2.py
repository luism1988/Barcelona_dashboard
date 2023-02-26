#Este documento es un prueba para  ir 
#viendo como funcionan los checkbox, etc..
import streamlit as st
import streamlit.components.v1 as components


st.title('BARCELONA DASHBOARD')
st.image('./barcelona_5.png')


st.text('Vamos a mostrar datos sobre??') 

chosen_one = st.multiselect('Elige pokemon', ["uno","dos","tres"], key="1")
st.text(f'{chosen_one[0]}')
click = st.button('Click me')

