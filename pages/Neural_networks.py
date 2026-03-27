import streamlit as st

st.title("Neural Network Model (Titanic Survival)")

st.header("Dataset & Features (ชุดข้อมูลและตัวแปร)")
st.write("ชุดข้อมูลที่ใช้คือ `Titanic-Dataset.csv` สำหรับทำนายโอกาสรอดชีวิตของผู้โดยสารเรือไททานิก โดยมีตัวแปร (Features) ดังนี้:")

st.markdown("""
**ตัวแปรตั้งต้นที่ใช้ฝึกสอน (Features):**
* **Pclass**: ระดับชั้นของผู้โดยสาร (1 = 1st, 2 = 2nd, 3 = 3rd)
* **Sex**: เพศ (ทำการ Map ข้อมูลเป็น Male=1, Female=0)
* **Age**: อายุของผู้โดยสาร 
* **SibSp**: จำนวนพี่น้องหรือคู่สมรสที่ร่วมเดินทางมาด้วย
* **Parch**: จำนวนพ่อแม่หรือบุตรที่ร่วมเดินทางมาด้วย
* **Fare**: ค่าโดยสาร
* **Embarked**: ท่าเรือที่ขึ้นเรือ (ทำ One-hot Encoding เป็น `Embarked_C`, `Embarked_Q`, `Embarked_S`)

**ตัวแปรเป้าหมาย (Target/Label):**
* **Survived**: สถานะการรอดชีวิต (1 = รอดชีวิต, 0 = ไม่รอด)
""")

st.header("Data Preparation")
st.markdown("""
* **Data Cleaning**: 
    * เติมค่าว่าง (Missing Values) ในคอลัมน์ `Age` และ `Fare` ด้วยค่ามัธยฐาน (Median)
    * เติมค่าว่างในคอลัมน์ `Embarked` ด้วยค่าฐานนิยม (Mode)
* **Feature Encoding**: 
    * แปลงข้อมูลเพศ (`Sex`) จากข้อความเป็นตัวเลข (Male=1, Female=0)
    * ทำ One-hot Encoding สำหรับตัวแปรท่าเรือ (`Embarked`) จะได้ 3 คอลัมน์ใหม่ 
* **Scaling**: ทำ Data Scaling ฟีเจอร์ทั้ง 9 ตัว โดยใช้ `StandardScaler` เพื่อปรับให้ข้อมูลมีค่าเฉลี่ยเป็น 0 และส่วนเบี่ยงเบนมาตรฐานเป็น 1 ช่วยให้ Neural Network เรียนรู้ได้มีประสิทธิภาพมากขึ้น
""")

st.header("Architecture")
st.markdown("""
โครงสร้างของ Neural Network สร้างแบบ Sequential จำนวน 9 Inputs โดยมีรายละเอียดดังนี้:
* **Hidden Layer 1**: ใช้ Dense Layer จำนวน 64 Nodes (Activation Function = `ReLU`)
* **Dropout Layer 1**: สุ่มดรอปเอาท์ 30% (Rate = 0.3) เพื่อลดอาการ Overfitting
* **Hidden Layer 2**: ใช้ Dense Layer จำนวน 32 Nodes (Activation Function = `ReLU`)
* **Dropout Layer 2**: สุ่มดรอปเอาท์ 20% (Rate = 0.2) เพื่อลดอาการ Overfitting
* **Output Layer**: ใช้ Dense Layer จำนวน 1 Node (Activation Function = `Sigmoid`) เพื่อแสดงค่าความน่าจะเป็น 0 ถึง 1 (รอด หรือ ไม่รอด)
""")

st.header("Development Steps")
st.markdown("""
* **Compile**: กำหนด Optimizer (Adam) และ Loss Function (`binary_crossentropy`) พร้อมวัดผลด้วย `accuracy`
* **Train & Evaluate**: โมเดลถูกเทรนและสามารถทำนายผลแม่นยำประมาณ 80.7% เมื่อใช้งานร่วมกับการทำ Standard Scaling
* **Export Model**: บันทึกโครงสร้างค่าน้ำหนักโมเดลให้อยู่ในรูปแบบ HDF5 (`.h5`) ในชื่อ `titanic_nn_model.h5`
""")

st.header("References (แหล่งอ้างอิง)")
st.markdown("""
* **Dataset:** Yasser H. (n.d.). *Titanic Dataset*. Kaggle. Retrieved from [https://www.kaggle.com/datasets/yasserh/titanic-dataset?resource=download](https://www.kaggle.com/datasets/yasserh/titanic-dataset?resource=download)
* **Library Documentation:** TensorFlow & Keras Documentation (`tf.keras.models.Sequential`, `tf.keras.layers.Dense`, `tf.keras.layers.Dropout`)
""")