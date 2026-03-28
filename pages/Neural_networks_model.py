import os
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

st.title("Neural Network (Titanic)")

@st.cache_data
def prepare_scaler():
    # หาที่อยู่ไฟล์ CSV
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, 'Titanic-Dataset.csv')
    
    df = pd.read_csv(csv_path)
    
    # 1. จัดการ Missing Values
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Fare'] = df['Fare'].fillna(df['Fare'].median())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    
    # 2. จัดการข้อมูล Category
    df['Sex'] = df['Sex'].map({'male': 1, 'female': 0})
    df = pd.get_dummies(df, columns=['Embarked'])
    
    # 3. เรียงลำดับคอลัมน์ให้ตรงกับตอนเทรน
    features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked_C', 'Embarked_Q', 'Embarked_S']
    
    X = df[features].astype(float)
    
    # 4. สร้างและ Train Scaler
    scaler = StandardScaler()
    scaler.fit(X)
    
    return scaler, features

# โหลด Scaler จาก Data ต้นฉบับ
scaler, feature_names = prepare_scaler()

# โหลดโมเดล (อ่านค่าน้ำหนักจากไฟล์ .pkl เพื่อลดขนาด dependency ไม่ต้องใช้ TensorFlow)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
weights_path = os.path.join(base_dir, 'titanic_weights.pkl')
with open(weights_path, 'rb') as f:
    nn_weights = pickle.load(f)

def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def predict_nn(X, weights):
    # Layer 1
    z1 = np.dot(X, weights[0]['W']) + weights[0]['b']
    a1 = relu(z1)
    # Layer 2
    z2 = np.dot(a1, weights[1]['W']) + weights[1]['b']
    a2 = relu(z2)
    # Layer 3
    z3 = np.dot(a2, weights[2]['W']) + weights[2]['b']
    a3 = sigmoid(z3)
    return a3

st.write("กรุณากรอกข้อมูลผู้โดยสารเพื่อประเมินโอกาสรอดชีวิตจากเหตุการณ์ไททานิก")

st.info("""💡 **ข้อเท็จจริงและข้อสังเกตที่สำคัญจาก Dataset:**

- สถิติพบว่า **ผู้หญิงมีอัตราการรอดชีวิตสูงถึง 74.20%** ในขณะที่ **ผู้ชายมีโอกาสรอดเพียง 18.89%** (จากกฎกู้ภัยของเรือ 'Women and Children First')
- ผู้โดยสารทุกคนที่มีค่าโดยสาร **มากกว่า $500** ไม่ว่าจะเป็นเพศใดก็ตาม **รอดชีวิตทั้งหมด**
- ผู้โดยสารชายทุกคนที่จ่ายค่าโดยสารระหว่าง **$200-$300** **เสียชีวิตทั้งหมด**
- ผู้โดยสารหญิงทุกคนที่จ่ายค่าโดยสารระหว่าง **$200-$300** **รอดชีวิตทั้งหมด**

🔗 **แหล่งอ้างอิงข้อมูลเพิ่มเติม:**
[How to score top 3% in Kaggle's Titanic ML Competition (Anel Music)](https://anelmusic13.medium.com/how-to-score-top-3-in-kaggles-titanic-machine-learning-from-disaster-competition-13d056e262b1)""")

col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox("ชั้นโดยสาร (Pclass)", [1, 2, 3])
    sex = st.selectbox("เพศ (Sex)", ["Male", "Female"])
    age = st.number_input("อายุ (Age)", min_value=0.0, max_value=120.0, value=30.0)
    embarked = st.selectbox("ท่าเรือที่ขึ้นเรือ (Port of Embarkation)", ["C (Cherbourg)", "Q (Queenstown)", "S (Southampton)"])

with col2:
    sibsp = st.number_input("พี่น้อง/คู่สมรสที่อยู่บนเรือ(SibSp)", min_value=0, max_value=10, value=0)
    parch = st.number_input("พ่อแม่/ลูกที่อยู่บนเรือ (Parch)", min_value=0, max_value=10, value=0)
    fare = st.number_input("ค่าโดยสาร (Passenger Fare ($))", min_value=0.0, max_value=600.0, value=32.0)

if st.button("ทำนาย"):
    # แปลงข้อมูลรับเข้า (Inputs)
    sex_val = 1 if sex == "Male" else 0
    embarked_c = 1 if embarked.startswith("C") else 0
    embarked_q = 1 if embarked.startswith("Q") else 0
    embarked_s = 1 if embarked.startswith("S") else 0
    
    # สร้าง DataFrame 1 row
    input_data = pd.DataFrame([[
        pclass, sex_val, age, sibsp, parch, fare, embarked_c, embarked_q, embarked_s
    ]], columns=feature_names).astype(float)
    
    # แปลงสเกล
    scaled_input = scaler.transform(input_data)
    
    # ทำนายผลด้วย Numpy (ช่วยให้แอปทำงานได้เร็วมากและไม่ต้องพึ่ง TensorFlow)
    prediction = predict_nn(scaled_input, nn_weights)
    prob = float(prediction[0][0])
    
    st.markdown("---")
    st.subheader("Prediction Result:")
    st.info(f"โอกาสในการรอดชีวิต (Probability): {prob:.4f}")
    
    if prob >= 0.5:
        st.success("แนวโน้ม: รอดชีวิต (Survived)")
    else:
        st.error("แนวโน้ม: ไม่รอดชีวิต (Not Survived)")