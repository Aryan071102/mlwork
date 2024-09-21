import streamlit as st
import joblib
import numpy as np
# Streamlit app title
st.title("Temperature Prediction App")
model = joblib.load('gbr_model.joblib')

# User input for rain, windspeed, and humidity
rain = st.number_input("Enter the rain (in mm):", min_value=0.0, step=0.1)
windspeed = st.number_input("Enter the windspeed (in km/h):", min_value=0, step=1)
humidity = st.number_input("Enter the relative humidity (%):", min_value=0, max_value=100, step=1)

# Prediction button
if st.button("Predict Temperature"):
    # Create a feature array for the prediction
    features = np.array([[rain, windspeed, humidity]])
    
    # Predict the temperature using the model
    predicted_temperature = model.predict(features)[0]
    
    # Display the result
    st.success(f"The predicted temperature is {predicted_temperature:.2f} °C")
