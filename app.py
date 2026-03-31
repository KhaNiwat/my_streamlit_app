import streamlit as st

st.set_page_config(
    page_title="Intelligent System Project",
    layout="wide"
)

st.title("Intelligent System Project")
st.divider()
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.page_link("pages/Machine_Learning.py", label="ML Heart Disease", icon="📖")
with col2:
    st.page_link("pages/Machine_Learning_Models.py", label="ML Heart Disease Model", icon="⚙️")
with col3:
    st.page_link("pages/Neural_networks.py", label="NN Titanic Survival", icon="📖")
with col4:
    st.page_link("pages/Neural_networks_model.py", label="NN Titanic Survival Model", icon="⚙️")
st.divider()

st.header("📖 บทนำ (Introduction)")
st.markdown("""
**รายวิชา Intelligent System (040613701)**  
เว็บไซต์นี้เป็นส่วนหนึ่งของการศึกษาวิชาระบบอัจฉริยะ (Intelligent System) ซึ่งมุ่งเน้นการศึกษาหลักการพื้นฐาน ตลอดจนการประยุกต์ใช้ **Machine Learning** และ **Neural Network** เพื่อแก้ปัญหาและวิเคราะห์ข้อมูลจากสถานการณ์ในโลกความเป็นจริง

**🎯 จุดประสงค์ของเว็บไซต์:**
- เพื่อเสริมสร้างความเข้าใจใน **ขั้นตอนการพัฒนาโมเดล AI** ตั้งแต่สเตปการเตรียมข้อมูล (Data Preparation) ไปจนถึงการนำไปใช้งานจริง (Deployment)
- เพื่ออธิบายทฤษฎีและแนวคิดพื้นฐานเบื้องหลังของศาสตร์ Machine Learning และ Neural Network
- เพื่อสาธิตกลไกและทดลองใช้งาน **ระบบพยากรณ์จริง** ให้เห็นความสามารถของตัวแบบทั้งสองแขนง
- เพื่อเปรียบเทียบและแสดงให้เห็น **ความแตกต่างของการใช้อัลกอริทึม (Algorithm)** ในแต่ละประเภท

**📚 เนื้อหาภายในเว็บไซต์:**
- **Introduction** – แนะนำอธิบายรายวิชา โครงสร้าง และวัตถุประสงค์ของการพัฒนาระบบ
- **Machine Learning Model** – อธิบายกระบวนการและรูปแบบการทำงานของโมเดลฝั่ง Machine Learning
- **Neural Network Model** – อธิบายโครงสร้างเครือข่ายประสาทเทียมและการประมวลผลของโมเดล Neural Network
""")

st.divider()



# --- About Us Section ---
st.header("👨‍💻 ผู้จัดทำ (About Us)")
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""
**จัดทำโดย:**
- **นายนิวัฒน์ เสียงใส**
- รหัสนักศึกษา: 6404062610294
- DE-RA ชั้นปีที่ 5
""")

with col_b:
    st.markdown("""
**อาจารย์ผู้สอน:**
- ดร.ณัฐกิตติ์ จิตรเอื้อตระกูล (NJR)
""")