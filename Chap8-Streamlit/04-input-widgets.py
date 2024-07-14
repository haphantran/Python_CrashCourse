import streamlit as st


st.title("My Amazing App")
st.header("Input Widgets")
st.subheader('Basic input widgets')

st.write("st.text_input can be used to get a single line text input.")
name = st.text_input("Enter your name", value="Ten cua ban")
st.write("You entered:", name)

st.write("st.text_area can be used to get a multi-line text input.")
feedback = st.text_area("Enter your feedback", value="Noi dung feedback")
st.write("You entered:", feedback)

# st.write("st.number_input can be used to get a number input.")
# age = st.number_input("Enter your age", min_value=1, max_value=100, value=25)
# st.write("You entered:", age)

# st.write("st.slider can be used to get a number input within a range.")
# temp = st.slider("Select a temperature", min_value=0, max_value=100, value=25)
# st.write("You selected:", temp)

# st.write("st.date_input can be used to get a date input.")
# date = st.date_input("Enter a date", value=None)
# st.write("You entered:", date)

# st.write("st.time_input can be used to get a time input.")
# time = st.time_input("Enter a time", value=None)
# st.write("You entered:", time)

# st.write("st.selectbox can be used to get a single option select box.")
# color = st.selectbox("Select a color", options=["Red", "Green", "Blue"])
# st.write("You selected:", color)

# st.write("st.multiselect can be used to get a multi-option select box.")
# colors = st.multiselect("Select colors", options=["Red", "Green", "Blue"])
# st.write("You selected:", colors)

# st.write("st.checkbox can be used to get a boolean input.")
# agree = st.checkbox("I agree to the terms and conditions")
# st.write("You agreed:", agree)

# st.write("st.radio can be used to get a single option radio button.")
# fruit = st.radio("Select a fruit", options=["Apple", "Banana", "Orange"])
# st.write("You selected:", fruit)

# st.write("st.button can be used to get a button input.")
# if st.button("Click Me"):
#     st.write("Button was clicked!")
