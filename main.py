import streamlit as st

st.title("Hi")
st.write("Hello World!")

st.header("Heading")

st.markdown("From markdown")

st.image("image1.png")

st.sidebar.title("menu")
st.sidebar.selectbox("Choose Option", ["Home", "About"])