import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

#Load the saved model
model_filename = 'heart_disease_model.sav'
heart_disease_model = pickle.load(open(model_filename, 'rb'))

#load the scaler
scaler_filename = 'scaler.sav'
scaler = pickle.load(open(scaler_filename, 'rb'))

#page title
st.title('Heart Disease prediction using ML By NishD® ❤📈')

#create input fields for all features
st.subheader('Please enter the following information: ')

age = st.number_input('Age',min_value=0, max_value=130, value=24)
sex = st.selectbox('Gender',['Male','Female'])
cp = st.selectbox('Chest pain types', ['Typical Angina', 'Atypical Angina','Non-anginal Pain','Asymptomatic'])
trestbps = st.number_input('Resting blood pressure',min_value=0,max_value=220,value=120)
chol = st.number_input('Serum Cholesterol in mg/dl', min_value=0, max_value=600, value=200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl',['No', 'Yes'])
restecg = st.selectbox('Resting Electrocardiographic Results',['Normal','Having ST-T wave abnormality','Showing probable or definite left ventricular hypertrophy (LVH)'])
thalach = st.number_input('Maximum heart rate achieved',min_value=0,max_value=220,value=150)
exang = st.selectbox('Exercise induced angina', ['No','Yes'])
oldpeak = st.number_input('ST depression induces by exercise relative to rest', min_value=0.0, max_value=10.0,value=0.0,step=0.1)
slope = st.selectbox('Slope of the peak exercise ST segment',['Upsloping', 'Flat', 'Downsloping'])
ca = st.selectbox('Number of major vessels coloredby fluroscopy',[0,1,2,3])
thal = st.selectbox('Thal',['Normal','Fixed defect','Reversable defect'])

#code for prediction
heart_diagnosis = ''

#creating a button for prediction
if st.button('Heart Disease Test Result'):
    #prepare input data
    input_data = {
        'Age': age,
        'Sex': 1 if sex == 'Male' else 0,
        'Chest pain type': ['Typical Angina', 'Atypical Angina','Non-anginal Pain','Asymptomatic'].index(cp) + 1,
        'BP': trestbps,
        'Cholesterol': chol,
        'FBS over 120': 1 if fbs == 'Yes' else 0,
        'EKG results': ['Normal','Having ST-T wave abnormality','Showing probable or definite left ventricular hypertrophy (LVH)'].index(restecg),
        'Max HR': thalach,
        'Exercise angina': 1 if exang == 'Yes' else 0,
        'ST depression': oldpeak,
        'Slope of ST': ['Upsloping', 'Flat', 'Downsloping'].index(slope) + 1,
        'Number of vessels fluro': ca,
        'Thallium': ['Normal','Fixed defect','Reversable defect'].index(thal) + 1
    }

    #conver to Dataframe
    input_df = pd.DataFrame([input_data])

    #scale the input
    scaled_input = scaler.transform(input_df)

    try:
        #make prediction
        heart_prediction = heart_disease_model.predict(scaled_input)

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart Disease'
        else:
            heart_diagnosis = 'The person does not have any heart Disease'

        st.success(heart_diagnosis)
    except AttributeError as e:
        st.error(f"AttributeError: {str(e)}")
        st.write(f"Methods available on heart_disease_model {dir(heart_disease_model)}")
    except Exception as e:
        st.error(f"An error occured: {str(e)}")


#Add a disclaimer
st.warning("Disclaimer: This app is for Educational purpose only.Always consult a medical professional for advices.")