import pandas as pd
import streamlit as st

st.header('Displaying dataframes')

data = pd.DataFrame({
    'Name':['Alice', 'Bob','John','David','Eve'],
    'Age':[24,27,30,34,20],
    'City':['New York','Paris','Prishtine','Houston','Berlin']
})

st.dataframe(data)