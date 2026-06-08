import streamlit as st
import pandas as pd
import plotly.express as px



books_df = pd.read_csv('file1.csv')

st.title("Bestselling books analysis")
st.write("this app analyzes the Amazon top selling books from 2009 to 2022.")

st.subheader("summary statistics")
total_books = books_df.shape[0]
unique_titles = books_df['Name'].nunique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()

col1 , col2, col3, col4 = st.columns(4)
col1.metric("total books", total_books)
col2.metric("unique title", unique_titles)
col3.metric("average rating", average_rating)
col4.metric("average prace", average_price)

st.subheader("Dataset Preview")
st.write(books_df.head())

col1, col2, = st.columns(2)

with col1:
    st.subheader("Top 10 books Titles")
    top_titles = books_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)
with col2:
    st.subheader("Top 10 Authors")
    top_authors = books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

st.subheader("Genre Distribution")
fig = px.pie(books_df, names="Genre", title="Most liked Genre (2009-2022)", color='Genre',
             color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Top 15 Authors by Counts of Books Published (2009-2022) ")
top_authors = books_df['Author'].value_counts().head(15).reset_index()
top_authors.columns = ['Author', 'Count']
fig = pd.bar(top_authors, x='count', y='Author', orientation='h', title="Top 15 Authors by Counts of Books Published",
             labels={'Counts': 'Counts of Books Published', 'Author': ' Author'}, color='Count',
             color_discrete_sequence=px.colors.sequential.Plasma
             )
st.plotly_chart(fig)

st.subheader("Filter Data by Genre")
genre_filter = st.selectbox('Select Genre', books_df['Genre'].unique())
filtered_df = books_df[books_df['Genre'] == genre_filter]
st.write(filtered_df)