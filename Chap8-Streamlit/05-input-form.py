import streamlit as st

st.title("Input Form")

# Add form components
name = st.text_input("Name")
age = st.number_input("Age", min_value=0, max_value=100)
email = st.text_input("Email")
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
hobbies = st.multiselect("Hobbies", ["Reading", "Sports", "Music", "Traveling"])

# Submit button
if st.button("Submit"):
    st.success(f"Name: {name}")
    st.success(f"Age: {age}")
    st.success(f"Email: {email}")
    st.success(f"Gender: {gender}")
    st.success(f"Hobbies: {', '.join(hobbies)}")