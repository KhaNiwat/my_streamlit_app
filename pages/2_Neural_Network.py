import streamlit as st

st.set_page_config(page_title="Neural Network Model", layout="wide")

# ปรับสไตล์ให้เรียบง่าย (Dark Mode)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    h1 { color: #ff4b4b; }
    h2 { color: #ff8a8a; margin-top: 30px; }
    h3 { color: #ff8a8a; }
    </style>
    """, unsafe_allow_html=True)

st.title("Neural Network: Deep Learning Analysis")
st.write("การวิเคราะห์ข้อมูลมะเร็งด้วยโครงข่ายประสาทเทียม")
st.markdown("---")

# --- ส่วนที่ 1: การเตรียมข้อมูล ---
st.header("1. การเตรียมข้อมูล (Data Preparation)")
st.write("มีการสร้างตัวแปรใหม่คือ 'radius_ratio' จากการคำนวณสัดส่วนระหว่างรัศมีเฉลี่ยและเส้นรอบวง เพื่อช่วยให้โมเดลเห็นความสัมพันธ์ทางกายภาพของเซลล์ได้ชัดเจนขึ้น จากนั้นจึงนำข้อมูลทั้งหมดเข้าสู่กระบวนการ Standardization เพื่อปรับค่าให้อยู่ในระดับที่เหมาะสมสำหรับการคำนวณในชั้น Hidden Layers")

st.code("""
# ขั้นตอน Feature Engineering จากโค้ด
df_fe['radius_ratio'] = df_fe['mean radius'] / (df_fe['mean perimeter'] + 1)
""", language='python')

st.markdown("---")

# --- ส่วนที่ 2: ทฤษฎีอัลกอริทึม ---
st.header("2. ทฤษฎีของอัลกอริทึม (Algorithm Theory)")
st.write("โครงสร้างหลักคือ Multi-Layer Perceptron (MLP) ซึ่งทำงานผ่านชั้นเลเยอร์ที่ซ้อนทับกัน:")
st.write("- ReLU (Rectified Linear Unit): ฟังก์ชันกระตุ้นในชั้นซ่อน ช่วยให้โครงข่ายเรียนรู้ลักษณะเด่นที่ซับซ้อนและลดปัญหาการหายไปของเกรเดียนต์")
st.write("- Sigmoid: ฟังก์ชันในชั้นผลลัพธ์ที่ใช้แปลงค่าสัญญาณไฟฟ้าให้อยู่ในรูปของความน่าจะเป็นระหว่าง 0 ถึง 1 สำหรับการจำแนกประเภท")
st.write("- Adam Optimizer: อัลกอริทึมการปรับค่าพารามิเตอร์แบบปรับตัวตามเวลา (Adaptive) เพื่อให้การเรียนรู้ลุเข้าสู่จุดที่เหมาะสมที่สุดได้รวดเร็ว")

st.markdown("---")

# --- ส่วนที่ 3: ขั้นตอนการพัฒนาโมเดล ---
st.header("3. ขั้นตอนการพัฒนาโมเดล (Model Development)")
st.write("การพัฒนาเริ่มต้นจากการออกแบบสถาปัตยกรรม Sequential ที่ประกอบด้วยชั้น Input, Hidden Layer 2 ชั้น และชั้น Output โดยมีการใช้เทคนิค Early Stopping เพื่อคอยติดตามค่า Loss ในส่วนของข้อมูลตรวจสอบ (Validation) หากไม่มีการพัฒนาที่ดีขึ้นในระยะเวลาที่กำหนด ระบบจะหยุดการฝึกฝนอัตโนมัติเพื่อป้องกันการเกิด Overfitting")

st.code("""
# สถาปัตยกรรมจากโค้ดจริง
model = Sequential([
    Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')
])
early_stop = EarlyStopping(monitor='val_loss', patience=5)
""", language='python')

st.markdown("---")

# --- ส่วนที่ 4: แหล่งอ้างอิงข้อมูล ---
st.header("4. แหล่งอ้างอิงข้อมูล (References)")
st.write("ชุดข้อมูลสำหรับการวิเคราะห์ (Synthetic Breast Cancer Dataset) ถูกสร้างขึ้นโดย Generative AI (ChatGPT) เพื่อจำลองสถานการณ์จริง")
st.write("การพัฒนาใช้โครงสร้างพื้นฐานจากเฟรมเวิร์ก TensorFlow และ Keras (Chollet, 2015)")