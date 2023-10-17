#! weather-forecast-data-app\venv\Scripts\python.exe
import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox and subheader
st.title("Weather Forecast for the Next Days🌤️" )
st.write("")
st.write("")
place = st.text_input("Place:", key="place")
forecast_days = st.slider(label="Forecast Days", min_value=1, max_value=5, 
                          key="forecast_days", 
                          help="Select the number of forecasted days")
data_to_show = st.selectbox(label="Select data to view", options=(
    "Temperature", "Sky"), key="data_to_show") 
st.write("")
st.write("")

if place:
    # Get the temperature / sky data
    try:
        filtered_data = get_data(place, forecast_days)

        if data_to_show == "Temperature":
            st.subheader(f"{data_to_show} for the next {str(forecast_days)}"\
    f" days in {place}")
            # Extracting temperatures
            temperatures = [dict["main"]["temp"] for dict in filtered_data]    
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature(C°)"})
            st.plotly_chart(figure)
            expander = st.expander("See explanation")
            expander.write("""
                           Current temperatures are shown in Celsius (C°) degrees. On the Y-axis we got the temperature and in the X-asis we got the time from 00:00 until 24:00 hours.
                           """)
            
        elif data_to_show == "Sky":
            st.subheader(f"{data_to_show} for the next {str(forecast_days)}"\
    f" days in {place}")            
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            images = {"Clear":"images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow":"images/snow.png"}
            images_paths = [images[sky_condition] for sky_condition in sky_conditions]
            st.image(images_paths, width=115)
    except KeyError:
            st.write("That place does not exist :(")
        