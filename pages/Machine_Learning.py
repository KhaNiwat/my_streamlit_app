import streamlit as st

st.title("Machine Learning (Ensemble) Model")

st.header("Dataset & Features (ชุดข้อมูลและตัวแปร)")
st.write("ชุดข้อมูลที่ใช้คือ `heart_dataset.csv` มีจำนวน 500 records โดยมีตัวแปร (Features) ที่เกี่ยวข้องกับสุขภาพและผลการตรวจร่างกาย ดังนี้:")

st.markdown("""
**ตัวแปรทางสถิติและข้อมูลทั่วไป (Features):**
* **Age**: อายุของผู้ป่วย
* **Sex**: เพศ (แปลงเป็น `Sex_Male` ผ่าน One-hot Encoding)
* **CP (Chest Pain Type)**: ประเภทอาการเจ็บหน้าอก (แปลงเป็น `CP_atypical angina`, `CP_non-anginal pain`, `CP_typical angina`)
* **Trestbps**: ความดันโลหิตขณะพัก (Resting blood pressure)
* **Chol**: ระดับคอเลสเตอรอลในเลือด
* **Thalach**: อัตราการเต้นของหัวใจสูงสุดที่ทำได้ (Maximum heart rate achieved)

**ตัวแปรเป้าหมาย (Target/Label):**
* **Target**: ความเสี่ยงในการเป็นโรคหัวใจ (1 = มีความเสี่ยง, 0 = ปกติ)
""")

st.header("Data Preparation")
st.markdown("""
* **Data Cleaning**: ลบคอลัมน์ที่มีค่าว่าง (Missing Values) มากกว่า 50% ออก เติมค่าว่างของข้อมูลตัวเลขด้วยค่ามัธยฐาน (Median) และข้อมูลหมวดหมู่ด้วยค่าฐานนิยม (Mode)
* **Feature Encoding**: ทำ One-hot Encoding สำหรับตัวแปรหมวดหมู่ (drop_first=True) และแปลงชนิดข้อมูล Boolean เป็นตัวเลข 0/1
* **Data Splitting**: แบ่งชุดข้อมูลเป็น Train 80% และ Test 20% โดยใช้ `stratify=y` เพื่อรักษาสัดส่วนของ Class ให้สมดุลกัน
""")

st.header("Ensemble Concept")
st.markdown("""
โมเดลนี้ใช้เทคนิค **Ensemble Learning** ชนิด **Voting Classifier (Soft Voting)** 
หลักการคือการนำผลลัพธ์ที่เป็น *ค่าความน่าจะเป็น (Probability)* จากโมเดลย่อยหลายๆ ตัวมาเฉลี่ยรวมกัน จากนั้นจึงตัดสินใจเลือก Class ที่มีค่าเฉลี่ยความน่าจะเป็นสูงสุด วิธีนี้ช่วยลดความผันผวนและเพิ่มความแม่นยำได้ดีกว่าการใช้โมเดลเดียว
""")

st.header("Models Used")
st.markdown("""
โมเดลย่อย (Estimators) ที่นำมาต่อรวมกัน มีทั้งหมด 3 ตัว ได้แก่:
1. **Logistic Regression**: ใช้งานร่วมกับ `StandardScaler` ในรูปแบบ Pipeline เพื่อปรับสเกลข้อมูลก่อนเทรน (กำหนด `max_iter=1000`)
2. **Random Forest Classifier**: โมเดลแบบต้นไม้ตัดสินใจหลายต้น (กำหนด `n_estimators=200`, `max_depth=5`)
3. **Gradient Boosting Classifier**: โมเดลที่เรียนรู้จากข้อผิดพลาดของรอบก่อนหน้า (กำหนด `n_estimators=200`, `learning_rate=0.05`, `max_depth=3`)
""")

st.header("Development Steps")
st.markdown("""
* **Train Base Models**: ฝึกสอนและวัดผลโมเดลเดี่ยวทีละตัวเพื่อเป็น Baseline (Logistic Regression = 64.0%, Random Forest = 72.0%, Gradient Boosting = 72.0%)
* **Train Ensemble**: สร้างและฝึกสอน `VotingClassifier` ด้วยโมเดลย่อยทั้ง 3 ตัว
* **Evaluate**: ประเมินผลลัพธ์บนชุดข้อมูล Test ได้ค่า Accuracy ของ Ensemble ที่ **70.0%** และมีการเปรียบเทียบประสิทธิภาพด้วย **ROC Curve** และค่า **AUC**
* **Export Model**: บันทึกโมเดลด้วยไลบรารี `joblib` เป็นไฟล์ `heart_model.pkl` เพื่อนำไปใช้งานต่อ
""")

st.header("References (แหล่งอ้างอิง)")
st.markdown("""
Dataset: heart_dataset สร้างขึ้นจาก chatgpt
""")