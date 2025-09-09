import pandas as pd
import numpy as np
import streamlit as st
import pickle

st.set_page_config(page_title='Home', layout='centered')
st.title('car price prediction app')
st.write('data from cardekho web scraping by github/krishnaik')


#Encode Standardize Predict
#load encoders and model
with open('views/label_encoders.pkl', 'rb') as f:
    label_encoders = pickle.load(f)

with open('views/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('views/rf_model.pkl', 'rb') as f:
    car_price_model = pickle.load(f)

with open('views/car_lookup.pkl', 'rb') as f:
    car_lookup = pickle.load(f)


#adding 'Brand' NON functional for ML
brand = st.selectbox("Select Car Brand", sorted(car_lookup.keys()))


available_models = sorted(car_lookup[brand].keys())
model = st.selectbox('Model', available_models)
 



feature_order = [
    'model','vehicle_age','km_driven','seller_type','fuel_type','transmission_type','mileage','engine','max_power','seats'
]

#scrollable Inputs for Categorical Features
seller_type = st.selectbox('Seller Type',['Dealer','Individual','Trustmark Dealer'])

fuel_options = sorted(car_lookup[brand][model]['fuel_type'])
fuel_type = st.selectbox('Fuel Type',fuel_options)

transmission_options = sorted(car_lookup[brand][model]['transmission_type'])
transmission_type = st.selectbox('Transmission Type', transmission_options)



#Numerical Inputs
vehicle_age = st.number_input('Vehicle Age', min_value=0.0)
km_driven = st.number_input('Kms Driven', min_value=0.0)
mileage = st.number_input('Mileage', min_value=0.0)

engine_options = sorted(car_lookup[brand][model]['engine'])
engine = st.selectbox('Engine-CC', engine_options)

power_options = sorted(car_lookup[brand][model]['max_power']) 
max_power = st.selectbox('Power-BHP',power_options )

seat_options = sorted(car_lookup[brand][model]['seats'])
seats = st.selectbox('No. of Seats',seat_options)





        



#adding buttons to the form
if st.button('Predict'):
    try:
    #encode categorical inputs
        encoded = [
            label_encoders['model'].transform([model])[0],
            vehicle_age,
            km_driven,
            label_encoders['seller_type'].transform([seller_type])[0],
            label_encoders['fuel_type'].transform([fuel_type])[0],
            label_encoders['transmission_type'].transform([transmission_type])[0],
            mileage,
            engine,
            max_power,
            seats
        ]

        #converting to array and scale
        encoded_flat = np.array([encoded])
        input_scaled = scaler.transform(encoded_flat)

        #predict
        prediction = car_price_model.predict(input_scaled)
        st.success(f'Predicted Price: {prediction[0]:,.2f}')

    except Exception as e:
        st.error(f"Something went wrong DUDE: {e}")