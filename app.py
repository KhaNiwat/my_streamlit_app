import streamlit as st

# ตั้งค่าหน้าหลัก
st.set_page_config(
    page_title="Heart Disease Prediction Project",
    layout="wide"
)




# --- Main Content ---
st.title("Intelligent System")
st.markdown("""
โปรเจกต์ **Machine Learning** และ **Neural Network** 
""")

st.divider()

# ส่วนที่ 1: สรุปภาพรวมโปรเจกต์ (Overview)
col1, col2 = st.columns([2, 1])


# ส่วนที่ 2: ไฮไลท์ของแต่ละโมเดล (Quick Links / Summary)
st.subheader("🚀 โมเดลที่พัฒนา")

m_col1, m_col2 = st.columns(2)

with m_col1:
    st.markdown("### 🤖 Machine Learning")
    st.write("ใช้ **Voting Classifier** (Logistic Regression, RF, SVM) เพื่อความแม่นยำและการตัดสินใจแบบกลุ่ม")
    if st.button("ไปที่หน้า Machine Learning"):
        st.switch_page("pages/1_Machine Learning.py")

with m_col2:
    st.markdown("### 🧠 Neural Network")
    st.write("ใช้ **Multi-Layer Perceptron (MLP)** โครงข่ายประสาทเทียมเพื่อหาความสัมพันธ์เชิงลึกของข้อมูล")
    if st.button("ไปที่หน้า Neural Network"):
        st.switch_page("pages/2_Neural_Network.py")

st.divider()

# ส่วนที่ 3: Footer หรือเครดิต
st.caption("พัฒนาโดย: Niwat Siangsai")