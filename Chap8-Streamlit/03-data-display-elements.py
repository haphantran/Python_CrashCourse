import streamlit as st
import pandas as pd

st.title("My Amazing App")
st.header("Data Display element")
st.write("st.write can display text, data, and other objects.")
# st.write("Displaying a number:", 42)
# st.write("This is a list:")
# st.write(["item 1", "item 2", "item 3"])

st.write("This is a dictionary:")
st.write({"key 1": "value 1", "key 2": "value 2"})
# import pandas as pd
df = pd.DataFrame({"col1": [1, 2,5,6,7,8,9], "col2": [3, 4,5,6,7,8,9]})

st.write(df)

st.write("st.metric can display a metric with a value and a description.")
st.metric("Temperature", "25 °C", "1.2 °C",delta_color="inverse")
st.metric("Sales", "$12,345", "-$500", delta_color="normal",label_visibility="visible")

st.write("This is a table:")
st.table(df)

data = {"name": "Alice", "age": 30, "city": "New York"}
st.write("This is a json similar to dictionary:")
st.json(data)

st.header("Example - Loading data from csv file")

st.write("Loading data from a csv file:")
df = pd.read_csv("../Chap6_pandas/data/student.csv")
st.write(df)
