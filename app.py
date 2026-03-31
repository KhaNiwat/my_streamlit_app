import streamlit as st
from streamlit_option_menu import option_menu

import views.Machine_Learning
import views.Machine_Learning_Models
import views.Neural_networks
import views.Neural_networks_model

st.set_page_config(
    page_title="Intelligent System Project",
    layout="wide"
)

# ซ่อนแถบ Sidebar เดิมของ Streamlit
st.markdown("""
    <style>
        [data-testid="collapsedControl"] {
            display: none;
        }
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

pages = ["Home", "ML Heart Disease", "ML Heart Model", "NN Titanic", "NN Titanic Model"]
icons = ["house", "book", "gear", "book", "gear"]

selected = option_menu(
    menu_title=None,
    options=pages,
    icons=icons,
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "transparent"},
        "icon": {"color": "white", "font-size": "14px"}, 
        "nav-link": {
            "font-size": "14px", 
            "text-align": "center", 
            "margin":"0px", 
            "color": "white"
        },
        "nav-link-selected": {
            "background-color": "transparent", 
            "color": "#ff4b4b", 
            "font-weight": "bold", 
            "border-bottom": "2px solid #ff4b4b", 
            "border-radius": "0px"
        },
    }
)

if selected == "Home":
    st.title("Intelligent System Project")
    st.divider()

    st.header("📖 บทนำ (Introduction)")
    st.markdown("""
    **รายวิชา Intelligent System (040613701)**  
    เว็บไซต์นี้เป็นส่วนหนึ่งของการศึกษาวิชาระบบอัจฉริยะ (Intelligent System) ซึ่งมุ่งเน้นการศึกษาหลักการพื้นฐาน ตลอดจนการประยุกต์ใช้ **Machine Learning** และ **Neural Network** เพื่อแก้ปัญหาและวิเคราะห์ข้อมูลจากสถานการณ์ในโลกความเป็นจริง

    **🎯 จุดประสงค์ของเว็บไซต์:**
    - เพื่อเสริมสร้างความเข้าใจใน **ขั้นตอนการพัฒนาโมเดล AI**
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

elif selected == "ML Heart Disease":
    views.Machine_Learning.render()

elif selected == "ML Heart Model":
    views.Machine_Learning_Models.render()

elif selected == "NN Titanic":
    views.Neural_networks.render()

elif selected == "NN Titanic Model":
    views.Neural_networks_model.render()