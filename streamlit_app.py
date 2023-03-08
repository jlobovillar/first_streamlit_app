import streamlit
import pandas

streamlit.title('My Parents New Healtly Diner')

streamlit.header('Breakfast Menu')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Crea tu propio batido de frutas 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Pongamos una lista de selección aquí para que puedan escoger la fruta que quieren incluir 
streamlit.multiselect("Recoger algunas frutas:", list(my_fruit_list.index)) 

# Mostrar la tabla en la página.
streamlit.dataframe(my_fruit_list)
