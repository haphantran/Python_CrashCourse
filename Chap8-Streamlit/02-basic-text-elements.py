import streamlit as st
import pandas as pd


st.title("My Amazing App")
st.header("Text element")
st.subheader("Something interesting")
st.text("This is some regular text.")
st.markdown("Here's some text with **bold** and _italic_ styles.")
st.code("print('Hello from Python!')", language="python")

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.write("Please refer to streamlit text API documentation for more details: [Streamlit Text API](https://docs.streamlit.io/library/api-reference/text)")