#! weather-forecast-data-app\venv\Scripts\python.exe
import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
st.write("")
st.write("")
place = st.text_input("Place:", key="place", value="somewhere")
forecast_days = st.slider(label="Forecast Days", min_value=1, max_value=5, 
                          key="forecast_days", 
                          help="Select the number of forecasted days")
data_to_show = st.selectbox(label="Select data to view", options=(
    "Temperature", "Weather"), key="data_to_show") 
st.write("")
st.write("")
st.subheader(f"{data_to_show} for the next {str(forecast_days)}"\
    f" days in {place}")


data = get_data(place, forecast_days, data_to_show)

# figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature(C°)"})
# st.plotly_chart(figure)
st.session_state
