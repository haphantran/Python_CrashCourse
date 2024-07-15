import streamlit as st
import requests

API_KEY=st.secrets["API_KEY"]


def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",  # Use metric for Celsius
    }
    response = requests.get(url, params=params)
    st.write(API_KEY)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error fetching weather data. Please check the city name.")
        return None


st.title("Weather App")

city = st.text_input("Enter a city name:")

if city:
    weather_data = get_weather_data(city)

    if weather_data:
        # Extract relevant data
        temp = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]
        icon = weather_data["weather"][0]["icon"]

        # Display weather information
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Temperature", f"{temp}°C")
            st.metric("Humidity", f"{humidity}%")
        with col2:
            st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png")
            st.write(description.capitalize())
