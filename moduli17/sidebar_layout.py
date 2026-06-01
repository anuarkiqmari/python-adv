import streamlit as st
from pydeck import settings

st.sidebar.header("sidebar")

st.sidebar.write("this is the sidebar")

st.sidebar.selectbox("choose an option", ["option1", "option2","option3"])

st.sidebar.radio("go to", ["home", "data", "settings"])
