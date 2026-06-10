import pandas as pd
import streamlit as st
import plotly.express as px

from moduli17.streamlit_forms import submit_button

books_df = pd.read_csv("file1.csv")

st.title("Bestselling Books Analysis")
st.write("This app analyses the Amazon Top selling Books from 2009 to 2022")

st.sidebar.header("Add New Book Data")
with st.sidebar.form("book_form"):
    new_name = st.text_input("Book Name")
    new_author = st.text_input("Author")
    new_user_rating = st.slider("User Rating", 0.0, 5.0, 0.0, 0.1 )
    new_reviews = st.number_input("Reviews", min_value=0, step=1)
    new_price = st.number_input("Price", min_value=0, step=1)
    new_year = st.number_input("Year", min_value=2009, max_value=2022, step=1)
    new_genre = st.selectbox("Genre", books_df['Genre'].unique())
    submit_button = st.form_submit_button(label="Add Book")

if submit_button:
    new_data = {
        'Name': new_name,
        'Author': new_author,
        'User Rating': new_user_rating,
        'Reviews': new_reviews,
        'Price': new_price,
        'Year': new_year,
        'Genre': new_genre,
    }

    books_df = pd.concat([pd.DataFrame(new_data,index=[0]),books_df], ignore_index=True)
    books_df.to_csv('file1.csv', index=False)
    st.sidebar.success("New Book added successfulli!")
