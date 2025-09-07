import pandas as pd
import numpy as np
import streamlit as st
import pickle

st.set_page_config(page_title='Home', layout='centered')
st.title('car price prediction app')
st.write('data from cardekho web scraping by github/krishnaik')




feature_order = [
    'model','vehicle_age','km_driven','seller_type','fuel_type','transmission_type','mileage','engine','max_power','seats'
]

#scrollable Inputs for Categorical Features
seller_type = st.selectbox('Seller Type',['Dealer','Individual','Trustmark Dealer'])
fuel_type = st.selectbox('Fuel Type',['Petrol','Diesel','CNG','LPG','Electric'])
transmission_type = st.selectbox('Transmission Type',['Manual','Automatic'])
model = st.selectbox('Model',['i20','Swift Dzire','Swift','Alto','City','Wagon R','Grand','Innova',
                              'Verna','i10','Ecosport','Polo','Baleno','Amaze','Ciaz','Eritga',
                              'Creta','XUV500','KWID','Vitara','Scorpio','Figo','Vento','Celerio',
                              'Duster','Bolero','Fortuner','Rapid','Jazz','BMW-3','Tiago','Santro',
                              'E-Class','Eeco','C-Class','BMW-5','WR-V','Safari','A4','Superb','Nexon',
                              'Go','RediGo','Ignis','KUV','ASpire','A6','Thar','Octavia','Civic',
                              'Venue','X1','XF','Rover','Elantra','Endeavour','Hexa','Compass','BMW-7',
                              'S-Class','Tigor','GL-Class','FreeStyle','CR-V','Seltos',
                              'KUV100','BMW-X5','Marazzo','BMW-X3','Audi-Q7','Harrier','Hector','BMW-6','Yaris',
                              'Cooper','Dzire VXI','Cayenne','XUV300','S-Presso','GLS','Triber',
                              'Tucson','redi-Go','Mercedes-CLS','Kicks','Glanza','Maruti-XL6','D-max','Volvo-XC','BMW-Z4',
                              'BMW-X4','Audi-A8','Lexus-ES','XC60','Volvo-S90','Jaguar-XE','Carnival','Volvo-XC90','Dzire ZXI',
                              'Continental','Honda-CR','Panamera','F-Pace','Alturas','X-Trail','MUX',
                              'Wrangler','Lexus-RX','Lexus-NX','Dzire LXI','Macan','Ghibli','Aura','GTC4Lusso',
                              'Altroz','Mercedes-C','Ghost','Quattroporte','Gurkha'])
 

#Numerical Inputs
vehicle_age = st.number_input('Vehicle Age', min_value=0.0)
km_driven = st.number_input('Kms Driven', min_value=0.0)
mileage = st.number_input('Mileage', min_value=0.0)
engine = st.number_input('Engine Capacity CC', min_value=0.0)
max_power =st.number_input('max_power BHP', min_value=0.0)
seats = st.number_input('Seats', min_value=0.0)

        

#Encode Standardize Predict
#load encoders and model
with open('models/label_encoders.pkl', 'rb') as f:
    label_encoders = pickle.load(f)

with open('models/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('models/rf_model.pkl', 'rb') as f:
    car_price_model = pickle.load(f)



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