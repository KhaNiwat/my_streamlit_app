import streamlit as st

st.set_page_config(page_title="Machine Learning Model", layout="wide")

st.title(" Machine Learning (Ensemble) Model")
st.markdown("---")


st.header("Heart Disease Prediction")


st.subheader("1. รายละเอียดของ Dataset")
st.write(
    "Dataset ที่ใช้เป็นข้อมูลสุขภาพของผู้ป่วยจำนวน **500 ราย** "
    "ประกอบด้วยคุณลักษณะ (Features) ที่สำคัญ ดังนี้:"
)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
**ตัวแปร Features:**
| Feature | คำอธิบาย |
|---------|----------|
| **Age** | อายุของผู้ป่วย |
| **Sex** | เพศ (Male / Female) |
| **CP (Chest Pain)** | ประเภทของอาการเจ็บหน้าอก |
| **Trestbps** | ความดันโลหิตขณะพัก |
| **Chol** | ระดับคอเลสเตอรอล |
| **Thalach** | อัตราการเต้นของหัวใจสูงสุด |
""")
with col2:
    st.markdown("""
**ตัวแปรเป้าหมาย (Target/Label):**

| ค่า | ความหมาย |
|-----|----------|
| **1** | เป็นโรคหัวใจ |
| **0** | ไม่เป็นโรคหัวใจ |

> Dataset: `heart_dataset.csv`
""")

st.markdown("---")


st.subheader("2. ขั้นตอน Data Preparation")
st.markdown("""
| ขั้นตอน | รายละเอียด |
|---------|-----------|
| **Handling Missing Values** | ตรวจสอบและจัดการค่าที่หายไป — เติมค่า **Median** สำหรับข้อมูลตัวเลข และ **Mode** สำหรับข้อมูลหมวดหมู่ |
| **Feature Selection** | ลบคอลัมน์ที่มีข้อมูลขาดหายมากกว่า **50%** ออก |
| **Data Transformation** | ทำ **One-hot Encoding** เพื่อแปลงข้อมูลหมวดหมู่ให้เป็นตัวเลข และใช้ **StandardScaler** สำหรับโมเดลที่ไวต่อสเกลข้อมูล (เช่น Logistic Regression) |
| **Data Splitting** | แบ่งชุดข้อมูลเป็น Train / Validation / Test ในสัดส่วน **80:10:10** หรือ **80:20** ตามลำดับการทดลอง โดยใช้ `stratify=y` รักษาสัดส่วน Class |
""")

st.markdown("---")


st.subheader("3. แนวคิดของ Ensemble Model")

col3, col4 = st.columns([2, 1])
with col3:
    st.markdown("""
**Ensemble Learning** คือเทคนิคการนำโมเดลหลายๆ ตัวมารวมพลังกันเพื่อทำนายผลลัพธ์ โดยมีจุดประสงค์เพื่อ:
- ลด **Bias** และ **Variance**
- เพิ่มความแม่นยำให้สูงกว่าการใช้โมเดลเพียงตัวเดียว

ในโปรเจกต์นี้ใช้เทคนิค **Soft Voting** ซึ่งเป็นการนำ **ค่าความน่าจะเป็น (Probability)** 
จากหลายโมเดลมาเฉลี่ยกัน แล้วเลือก Class ที่มีค่าเฉลี่ยสูงสุดเป็นผลลัพธ์สุดท้าย
""")
with col4:
    st.info("""
**Voting Types:**
- 🔵 **Hard Voting**: โหวตโดยตรงจากผล Class
- 🟢 **Soft Voting**: เฉลี่ย Probability 
""")

st.markdown("---")


st.subheader("4. โมเดลที่ใช้พัฒนา (อย่างน้อย 3 ตัว)")

col5, col6, col7 = st.columns(3)

with col5:
    st.markdown("""
### Logistic Regression
โมเดลพื้นฐานสำหรับการจำแนกประเภทเชิงเส้น

**พารามิเตอร์:**
- `max_iter = 1000`
- ใช้ร่วมกับ `StandardScaler` ใน Pipeline

**ข้อดี:** เรียบง่าย, ตีความได้ง่าย, ทำงานได้ดีกับข้อมูลเชิงเส้น
""")

with col6:
    st.markdown("""
### Random Forest
โมเดลแบบ Ensemble (Bagging) ที่ใช้ Decision Trees หลายต้น

**พารามิเตอร์:**
- `n_estimators = 200`
- `max_depth = 5`

**ข้อดี:** ลด Overfitting ได้ดี, ทนทานต่อ Outlier
""")

with col7:
    st.markdown("""
###  Gradient Boosting
โมเดลแบบ Ensemble (Boosting) ที่สร้างโมเดลใหม่เพื่อแก้ข้อผิดพลาดก่อนหน้า

**พารามิเตอร์:**
- `n_estimators = 200`
- `learning_rate = 0.05`
- `max_depth = 3`

**ข้อดี:** Accuracy สูง, จัดการ Non-linear ได้ดี
""")

st.markdown("---")


st.subheader("5. ขั้นตอนการพัฒนาโมเดล")

steps = {
    "🔹 Base Modeling": "ฝึกสอนโมเดลพื้นฐานทีละตัวเพื่อดูประสิทธิภาพเริ่มต้น (Baseline) — LR = 64.0%, RF = 72.0%, GB = 72.0%",
    "🔹 Hyperparameter Tuning": "ใช้ **GridSearchCV** เพื่อค้นหาค่าพารามิเตอร์ที่ดีที่สุดสำหรับ Random Forest และ Gradient Boosting โดยเน้นเพิ่มค่า **F1-Score**",
    "🔹 Ensemble Integration": "รวมโมเดลที่ผ่านการจูนแล้วทั้ง 3 ตัวเข้าด้วยกันผ่าน **VotingClassifier** (Soft Voting)",
    "🔹 Evaluation": "ประเมินผลด้วย **Accuracy**, **F1-Score** และ **ROC Curve** เพื่อเปรียบเทียบประสิทธิภาพ — Ensemble Accuracy = **70.0%**",
    "🔹 Export Model": "บันทึกโมเดลด้วย `joblib` เป็นไฟล์ `heart_model.pkl` เพื่อนำไปใช้งานต่อ",
}

for step, desc in steps.items():
    with st.expander(step):
        st.markdown(desc)

st.markdown("---")


st.subheader("6. แหล่งอ้างอิง (References)")
st.markdown("""
| แหล่งอ้างอิง | ลิงก์ |
|-------------|------|
|  UCI ML Repository / Kaggle | Machine Learning Concepts & Heart Disease Dataset |
| Dataset | `heart_dataset.csv` (สร้างขึ้นจาก ChatGPT) |
""")

st.markdown("---")
st.caption("Ensemble Model สำหรับการทำนายโรคหัวใจ ")