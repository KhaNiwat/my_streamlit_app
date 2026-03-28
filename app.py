import streamlit as st

st.set_page_config(
    page_title="Intelligent System Project",
    page_icon=" ",
    layout="wide"
)

st.title("Intelligent System Project")
st.divider()

# Section: Machine Learning
st.header("🫀 Machine Learning (Heart Disease)")
st.markdown("ทำนายความเสี่ยงโรคหัวใจด้วยเทคนิค **Ensemble Learning**")

col1, col2 = st.columns(2)
with col1:
    st.info("อธิบายทฤษฎีและขั้นตอนการเตรียมข้อมูล")
    # ตรวจสอบชื่อไฟล์ Machine_Learning.py (M และ L ตัวใหญ่)
    st.page_link("pages/Machine_Learning.py", label="ดูรายละเอียดโมเดล ML")
with col2:
    st.success("ทดลองใช้งานระบบทำนายผลจริง")
    # ตรวจสอบชื่อไฟล์ Machine_Learning_Models.py
    st.page_link("pages/Machine_Learning_Models.py", label="ใช้งานโมเดล ML")

st.write("")

# Section: Neural Networks
st.header("🚢 Neural Networks (Titanic Survival)")
st.markdown("ประเมินโอกาสรอดชีวิตจากเหตุการณ์ไททานิกด้วย **ANN**")

col3, col4 = st.columns(2)
with col3:
    st.info("อธิบายโครงสร้าง Deep Learning และการจัดการ Features")
    # แก้ไขตรงนี้ให้ตรงกับชื่อไฟล์จริง (ตรวจสอบ N ตัวใหญ่)
    st.page_link("pages/Neural_networks.py", label="ดูรายละเอียดโมเดล NN")
with col4:
    st.warning("ทดลองจำลองข้อมูลผู้โดยสารเพื่อทำนายผล")
    # ตรวจสอบชื่อไฟล์ Neural_networks_model.py
    st.page_link("pages/Neural_networks_model.py", label="ใช้งานโมเดล NN")

st.divider()
st.caption("© 2026 Intelligent System Project By. Mr.Niwat Siangsai")