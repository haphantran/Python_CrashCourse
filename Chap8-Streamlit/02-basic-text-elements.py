import streamlit as st
import pandas as pd


st.title("My Amazing App")
st.header("Text element")
st.subheader("Something interesting")
st.text("This is some regular text.")
st.markdown("Here's some text with **bold** and *italic* styles.")
st.code("print('Hello from Python!')", language="python")



st.write("Please refer to streamlit text API documentation for more details: [Streamlit Text API](https://docs.streamlit.io/library/api-reference/text)")