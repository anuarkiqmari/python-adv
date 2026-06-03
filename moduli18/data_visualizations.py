import streamlit as st
import pandas as pd
import plotly.express as ps

from moduli13.pandas_series import total_sales

books_df = pd.read_csv('file1.csv')

st.title("Bestselling books analysis")
st.write("this app analyzes the Amazon top selling books from 2009 to 2022.")

st.subheader("summary statistics")
total_books = books_df.shape[0]
unique_titles = books_df['name'].nunique()