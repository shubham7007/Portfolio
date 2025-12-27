import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.models import load_model
import streamlit as st


st.set_page_config(page_title='Home', layout='centered')
st.title('Customer Churn Prediction ANN ')
st.write('data from github/krishnaik')

#loading the trained model
model = load_model('models/ANN/model_updated.h5')

with open('models/ANN/onehot_encoder_geo.pkl','rb') as file:
    onehot_encoder_geo = pickle.load(file)

with open('models/ANN/label_encoder_gender.pkl','rb') as file:
    label_encoder_gender = pickle.load(file)

with open('models/ANN/scaler.pkl','rb') as file:
    scaler = pickle.load(file)



CreditScore = st.number_input('Credit Score', min_value=0)
Geography = st.selectbox('Geography', ['France', 'Germany', 'Spain'], index=0)
Gender = st.selectbox('Gender', ['Male', 'Female'])
Age = st.number_input('Age', min_value=1)
Tenure = st.number_input('Tenure', min_value=0)
Balance = st.number_input('Balance', min_value=1)
NumOfProducts = st.number_input('Number Of Products', min_value=1)
# HasCrCard = st.number_input('Has Credit Card', min_value=0)
HasCrCard = st.selectbox('Has Credit Card', ['Yes', 'No'])
HasCrCard = 1 if HasCrCard == 'Yes' else 0
IsActiveMember = st.selectbox('Is Active Member', ['Yes', 'No'])
IsActiveMember = 1 if IsActiveMember == 'Yes' else 0
EstimatedSalary = st.number_input('Estimated Salary', min_value=1)



#adding buttons to the form 
if st.button('Predict'):
    #validation Check

    missing_fields = []
    if Geography == '':
        missing_fields.append('Geography')
    if Gender == []:
        missing_fields.append('Gender')
    if HasCrCard == '':
        missing_fields.append('HasCrCard')
    if IsActiveMember == '':
        missing_fields.append('IsActiveMember')

    if missing_fields:
        st.warning(f"please fill all required fields: {', '.join(missing_fields)}")
    else:


        try:
        #encode categorical inputs

            geo_encoded = onehot_encoder_geo.transform([[Geography]]).toarray()[0]
            gender_encoded = label_encoder_gender.transform([Gender])[0]
            encoded = [
                CreditScore,
                *geo_encoded,
                gender_encoded,
                Age,
                Tenure,
                Balance,
                NumOfProducts,
                HasCrCard,
                IsActiveMember,
                EstimatedSalary
            ] 

            #converting to array and scale
            encoded_flat = np.array([encoded])
            input_scaled = scaler.transform(encoded_flat)

            #prediction
            prediction = model.predict(input_scaled)
            prediction_proba = prediction[0][0]

            if prediction_proba > 0.5 :
                st.write('The Customer is likely to come')
            else:
                st.write('The customer will not return')
        
        except Exception as e:
            st.error(f"Something Went Wrong Buddy: {e}")


## Footer
st.markdown('-----------------')
st.caption("Built using ANN + TensorFlow + Streamlit")