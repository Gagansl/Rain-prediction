import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model
model = pickle.load(open('model.pkl', 'rb'))

# Title of the app
st.title('Rain Prediction')

# Example for 18 features (modify based on your model's feature set)
temperature = st.number_input('Temperature (°C)', min_value=-50.0, max_value=50.0, value=25.0)
humidity = st.number_input('Humidity (%)', min_value=0, max_value=100, value=60)
wind_speed = st.number_input('Wind Speed (km/h)', min_value=0.0, max_value=100.0, value=10.0)
pressure = st.number_input('Pressure (hPa)', min_value=900, max_value=1100, value=1013)
# Add more input fields here based on the model's requirements...

# Collecting all inputs into a list with the required number of features
# Assuming X_test contains the 18 features
inputs = np.array([temperature, humidity, wind_speed, pressure]).reshape(1, -1)  # Match the model's expected input
prediction = model.predict(inputs)




# Button to make predictions
if st.button('Predict Rain'):
    prediction = model.predict(inputs)
    
    if prediction[0] == 1:
        st.write('Rain Prediction: **Yes**')
    else:
        st.write('Rain Prediction: **No**')

