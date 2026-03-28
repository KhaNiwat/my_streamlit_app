import streamlit as st

st.set_page_config(page_title="Neural Network Model - Titanic", layout="wide")

st.title("🚢 Neural Network Model (Titanic Survival)")
st.markdown("---")


st.header("1. Dataset & Features (ชุดข้อมูลและตัวแปร)")
st.write("ชุดข้อมูลที่ใช้คือ `Titanic-Dataset.csv` สำหรับทำนายโอกาสรอดชีวิตของผู้โดยสารเรือไททานิก โดยมีตัวแปร (Features) ดังนี้:")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
**ตัวแปรตั้งต้นที่ใช้ฝึกสอน (Features):**

| Feature | คำอธิบาย |
|---------|----------|
| **Pclass** | ระดับชั้นของผู้โดยสาร (1 = 1st, 2 = 2nd, 3 = 3rd) |
| **Sex** | เพศ (Map เป็น Male=1, Female=0) |
| **Age** | อายุของผู้โดยสาร |
| **SibSp** | จำนวนพี่น้อง/คู่สมรสที่ร่วมเดินทาง |
| **Parch** | จำนวนพ่อแม่/บุตรที่ร่วมเดินทาง |
| **Fare** | ค่าโดยสาร |
| **Embarked** | ท่าเรือที่ขึ้นเรือ (One-hot: `C`, `Q`, `S`) |
""")
with col2:
    st.markdown("""
**ตัวแปรเป้าหมาย (Target/Label):**

| ค่า | ความหมาย |
|-----|----------|
| **1** | รอดชีวิต |
| **0** | ไม่รอดชีวิต |

> Dataset: `Titanic-Dataset.csv`  
> แหล่งที่มา: [Kaggle - Titanic Dataset](https://www.kaggle.com/c/titanic)
""")

st.markdown("---")


st.header("2. Data Preparation (ขั้นตอนการเตรียมข้อมูล)")
st.markdown("""
| ขั้นตอน | รายละเอียด |
|---------|-----------|
| **Data Cleaning** | เติมค่าว่างในคอลัมน์ `Age` และ `Fare` ด้วยค่า **Median** และคอลัมน์ `Embarked` ด้วยค่า **Mode** |
| **Feature Encoding** | แปลงเพศ (`Sex`) เป็นตัวเลข (Male=1, Female=0) และทำ **One-hot Encoding** สำหรับ `Embarked` |
| **Feature Scaling** | ใช้ `StandardScaler` ปรับข้อมูลทุก Feature ให้มีค่าเฉลี่ย = 0 และ SD = 1 เพื่อให้ Neural Network เรียนรู้ได้มีประสิทธิภาพมากขึ้น |
| **Data Splitting** | แบ่งข้อมูลเป็น Train / Validation / Test เพื่อประเมินประสิทธิภาพโมเดลอย่างถูกต้อง |
""")

st.markdown("---")


st.header("3. Neural Network Architecture")
st.write("โครงสร้างของ Neural Network สร้างแบบ **Sequential** จำนวน **9 Inputs** โดยมีรายละเอียดดังนี้:")

col3, col4 = st.columns([3, 2])
with col3:
    st.markdown("""
| Layer | รายละเอียด |
|-------|-----------|
| **Input** | 9 Features (หลัง Encoding & Scaling) |
| **Hidden Layer 1** | Dense 64 Nodes — Activation: `ReLU` |
| **Dropout Layer 1** | Rate = 0.3 (ดรอป 30%) เพื่อลด Overfitting |
| **Hidden Layer 2** | Dense 32 Nodes — Activation: `ReLU` |
| **Dropout Layer 2** | Rate = 0.2 (ดรอป 20%) เพื่อลด Overfitting |
| **Output Layer** | Dense 1 Node — Activation: `Sigmoid` (ค่าความน่าจะเป็น 0–1) |
""")
with col4:
    st.info("""
**Compile Settings:**
- **Optimizer**: Adam
- **Loss Function**: `binary_crossentropy`
- **Metric**: `accuracy`
""")

st.markdown("---")


st.header("4. ขั้นตอนการพัฒนา (Development Steps)")
st.write("ขั้นตอนการพัฒนาโมเดลนี้ประกอบด้วย:")

titanic_steps = [
    (
        "🔹 1. การโหลดและทำความเข้าใจข้อมูล",
        """เริ่มต้นด้วยการโหลดชุดข้อมูล Titanic และสำรวจโครงสร้างของข้อมูล รวมถึง:
- ตรวจสอบข้อมูลที่ **ขาดหายไป (Missing Values)**
- ดูประเภทของข้อมูล (Categorical / Numerical)
- วิเคราะห์การกระจายตัวของข้อมูลเบื้องต้น""",
    ),
    (
        "🔹 2. การเตรียมข้อมูล",
        """ดำเนินการประมวลผลข้อมูลก่อนนำเข้าโมเดล ตามที่อธิบายไว้ในส่วน 'ขั้นตอนการเตรียมข้อมูล' ได้แก่:
- **Feature Engineering**: สร้างฟีเจอร์ใหม่จากข้อมูลที่มีอยู่
- **Handling Missing Values**: จัดการค่าที่ขาดหายไปด้วย Median / Mode
- **Categorical Encoding**: เข้ารหัสข้อมูลหมวดหมู่ให้เป็นตัวเลข
- **Feature Scaling**: ปรับขนาดข้อมูลเพื่อให้โมเดล Neural Network ทำงานได้ดีขึ้น""",
    ),
    (
        "🔹 3. การสร้างและฝึกโมเดล Neural Network",
        """ออกแบบโครงสร้าง Neural Network ด้วย **Keras / TensorFlow** กำหนดเลเยอร์ ฟังก์ชันกระตุ้น และ Dropout Layer จากนั้นทำการ Compile และฝึกโมเดลโดยใช้ชุดข้อมูลฝึกและชุดข้อมูล Validation:
- กำหนด **Layer** ต่างๆ (Input → Hidden → Dropout → Output)
- เลือก **Activation Function**: `ReLU` สำหรับ Hidden Layer, `Sigmoid` สำหรับ Output
- เพิ่ม **Dropout Layer** เพื่อลด Overfitting
- **Compile** โมเดลด้วย Adam Optimizer และ Binary Crossentropy Loss
- **ฝึกโมเดล** โดยใช้ Training Set และ Validation Set""",
    ),
    (
        "🔹 4. การประเมินผลโมเดล",
        """หลังจากฝึกโมเดลเสร็จสิ้น จะทำการประเมินประสิทธิภาพของโมเดลบนชุดข้อมูลทดสอบ (Test Set) ที่โมเดลไม่เคยเห็นมาก่อน โดยใช้:

| เครื่องมือ | วัตถุประสงค์ |
|-----------|------------|
| **Confusion Matrix** | ดูจำนวน True Positives, True Negatives, False Positives และ False Negatives |
| **Classification Report** | คำนวณค่า Precision, Recall, F1-score และ Support สำหรับแต่ละ Class (รอดชีวิตและไม่รอดชีวิต) |
| **Accuracy Curve** | พล็อตเส้นกราฟแสดงแนวโน้มของ Training และ Validation Accuracy ตลอด Epochs เพื่อวิเคราะห์การเรียนรู้และตรวจจับ Overfitting |

>  **ผลลัพธ์:** โมเดลสามารถทำนายได้ความแม่นยำประมาณ **80.7%** บน Test Set""",
    ),
    (
        "🔹 5. การบันทึกโมเดล",
        """บันทึกโมเดลที่ฝึกแล้วลงในไฟล์ **`.h5`** (HDF5 format) เพื่อ:
- นำไปใช้งานทำนายผลจริง
- ปรับปรุงหรือ Fine-tune ในอนาคต
- แชร์ให้ทีมหรือนำ Deploy บน Production

>  ชื่อไฟล์: `titanic_nn_model.h5`""",
    ),
]

for title, content in titanic_steps:
    with st.expander(title):
        st.markdown(content)

st.markdown("---")


st.header("5. แหล่งอ้างอิง (References)")
st.markdown("""
| แหล่งอ้างอิง | ลิงก์ |
|-------------|------|
|  Kaggle Titanic - Machine Learning from Disaster | [kaggle.com/c/titanic](https://www.kaggle.com/c/titanic) |
|  TensorFlow Documentation | [tensorflow.org/api_docs](https://www.tensorflow.org/api_docs) |
|  scikit-learn Documentation | [scikit-learn.org/stable/documentation.html](https://scikit-learn.org/stable/documentation.html) |
|  Pandas Documentation | [pandas.pydata.org/docs](https://pandas.pydata.org/docs/) |
|  Dataset | Yasser H. *Titanic Dataset* — [Kaggle](https://www.kaggle.com/datasets/yasserh/titanic-dataset) |
""")

st.markdown("---")
st.caption("Neural Network Model สำหรับการทำนายการรอดชีวิตของผู้โดยสาร Titanic")