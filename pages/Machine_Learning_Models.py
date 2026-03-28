import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("Machine_Learning (Heart Disease)")

model = joblib.load('heart_model.pkl')

st.write("กรุณากรอกข้อมูลสุขภาพเพื่อทำนายความเสี่ยงโรคหัวใจ")

st.info("""💡 **แหล่งข้อมูลและข้อสังเกตเบื้องต้น:**
- **ชุดข้อมูลอ้างอิง:** อิงแนวคิดจาก [UCI Heart Disease Dataset](https://archive.ics.uci.edu/dataset/45/heart+disease) (Cleveland Clinic Foundation) ซึ่งเป็นชุดข้อมูลมาตรฐานสากลด้าน Machine Learning
- **ปัจจัยเสี่ยงที่สำคัญ:** จากสถิติมักพบว่า **ผู้ชายมีความเสี่ยงสูงกว่าผู้หญิง** รวมถึงผู้ที่มีอาการ **เจ็บหน้าอก (Chest Pain)** ชนิดต่างๆ และ **ระดับคอเลสเตอรอลที่สูงเกิน 200 mg/dl** มีผลต่อน้ำหนักในการทำนายความเสี่ยง
- ชุดข้อมูลที่ใช้สอนโมเดลนี้เป็น **ข้อมูลจำลอง (Synthetic Data)** ที่อิงจากค่าสถิติทางการแพทย์เพื่อใช้ในการศึกษาการรวมโมเดลแบบ **Ensemble Learning**""")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("อายุ", min_value=1.0, max_value=120.0, value=50.0)
    sex = st.selectbox("เพศ", ["Female", "Male"])
    cp = st.selectbox("ประเภทของอาการเจ็บหน้าอก (CP)", ["asymptomatic", "atypical angina", "non-anginal pain", "typical angina"])

with col2:
    trestbps = st.number_input("ความดันโลหิตขณะพัก (Trestbps)", min_value=50.0, max_value=250.0, value=120.0)
    chol = st.number_input("คอเลสเตอรอล (Chol)", min_value=100.0, max_value=600.0, value=200.0)
    thalach = st.number_input("อัตราการเต้นของหัวใจสูงสุด (Thalach)", min_value=50.0, max_value=250.0, value=150.0)

if st.button("ทำนาย"):
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