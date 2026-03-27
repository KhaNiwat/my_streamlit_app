import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("Machine_Learning (Heart Disease)")

model = joblib.load('models/heart_model.pkl')

st.write("กรุณากรอกข้อมูลสุขภาพเพื่อทำนายความเสี่ยงโรคหัวใจ")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1.0, max_value=120.0, value=50.0)
    sex = st.selectbox("Sex", ["Female", "Male"])
    cp = st.selectbox("Chest Pain Type (CP)", ["asymptomatic", "atypical angina", "non-anginal pain", "typical angina"])

with col2:
    trestbps = st.number_input("Resting Blood Pressure (Trestbps)", min_value=50.0, max_value=250.0, value=120.0)
    chol = st.number_input("Cholesterol (Chol)", min_value=100.0, max_value=600.0, value=200.0)
    thalach = st.number_input("Maximum Heart Rate (Thalach)", min_value=50.0, max_value=250.0, value=150.0)

if st.button("Predict ML Model"):
    sex_male = 1 if sex == "Male" else 0
    cp_atypical = 1 if cp == "atypical angina" else 0
    cp_non_anginal = 1 if cp == "non-anginal pain" else 0
    cp_typical = 1 if cp == "typical angina" else 0
    
    input_data = pd.DataFrame([[
        age, trestbps, chol, thalach, sex_male, cp_atypical, cp_non_anginal, cp_typical
    ]], columns=['Age', 'Trestbps', 'Chol', 'Thalach', 'Sex_Male', 'CP_atypical angina', 'CP_non-anginal pain', 'CP_typical angina'])
    
    prediction = model.predict(input_data)
    
    st.markdown("---")
    st.subheader("Prediction Result:")
    if prediction[0] == 1:
        st.error("มีความเสี่ยงเป็นโรคหัวใจ (Class 1)")
    else:
        st.success("ไม่มีความเสี่ยง (Class 0)")