
import streamlit

streamlit.title('My Parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('Blueberry oatmeal')
streamlit.header('💚❤️💙Favorites')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.multiselect("pick some fruits", list(my_fruit_list.index))
stream-lit.dataframe(my_fruit_list)
