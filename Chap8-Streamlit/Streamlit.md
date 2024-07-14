# Introduction

## What is Streamlit?

- A Python library for creating web apps, particularly for data science and machine learning projects.
- Minimal code required to get started; focus is on the data and analysis, not web dev intricacies.
- Open-source and actively developed community.

## Why Streamlit?

- Rapid prototyping and sharing of interactive results.
- Excellent for showcasing data insights, model predictions, and analyses.
- Intuitive interface for users without web development experience.

# Getting started

## Install

```bash
pip install streamlit
```

## Basic App structure

```python
import streamlit as st

st.title("My First Streamlit App")
st.write("Hello, world!")
```
## Widgets

- **Text Elements**: st.title, st.header, st.subheader, st.text, st.markdown, st.latex, st.code

- **Data Display**: st.write, st.dataframe, st.table, st.json, st.image

- **Charts**: Integration with libraries like Matplotlib, Plotly, Altair, etc.

- **Input Widgets**: st.button, st.slider, st.text_input, st.selectbox, st.multiselect, st.number_input, st.checkbox, st.radio, st.file_uploader

