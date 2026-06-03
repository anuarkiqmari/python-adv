import pandas as pd
import streamlit as st

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'charlie'],
    'age':[24,22,27],
    'city':['los angeles', 'new york', 'prishtine']
})

st.write(df)