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

# ปรับแต่ง CSS หลักของเว็บไซต์ (ซ่อน Sidebar และปรับความกว้าง/ระยะขอบ)
st.markdown("""
    <style>
        [data-testid="collapsedControl"] {
            display: none;
        }
        [data-testid="stSidebar"] {
            display: none;
        }
        /* ปรับความกว้างหน้าจอและความสูงด้านบน-ล่างให้กระชับขึ้น */
        .block-container {
            max-width: 1300px !important;
            padding-top: 2rem !important;
            padding-bottom: 2rem !important;
        }
        /* ทำให้แถบเมนู Option Menu ล็อกติดอยู่ด้านบนสุดเวลาเลื่อนจอ (Sticky Header) */
        div[data-testid="stElementContainer"]:has(iframe[title="streamlit_option_menu.option_menu"]) {
            position: sticky;
            top: 2.5rem; /* ระยะห่างจากขอบบนสุดตอนเลื่อน */
            z-index: 999; /* ให้อยู่เลเยอร์บนสุด */
            background-color: var(--background-color); /* เปลี่ยนสีพื้นหลังรองรับทั้ง Light และ Dark Mode อัตโนมัติ */
            padding-top: 10px;
            padding-bottom: 15px;
            margin-top: -10px;
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
        "container": {
            "padding": "0!important", 
            "background-color": "transparent",
            "max-width": "100%"
        },
        "icon": {"font-size": "14px"}, 
        "nav-link": {
            "font-size": "14px", 
            "text-align": "center", 
            "margin":"0px", 
            "padding": "10px",
            "white-space": "nowrap"
        },
        "nav-link-selected": {
            "background-color": "transparent", 
            "color": "#e03131", 
            "font-weight": "bold", 
            "border-bottom": "2px solid #e03131", 
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
    เว็บไซต์นี้เป็นส่วนหนึ่งของการศึกษาวิชาระบบอัจฉริยะ (Intelligent System) ซึ่งมุ่งเน้นการศึกษาหลักการพื้นฐาน ตลอดจนการประยุกต์ใช้ **Machine Learning** และ **Neural Network**

    **🎯 จุดประสงค์ของเว็บไซต์:**
    - เพื่อเสริมสร้างความเข้าใจใน **ขั้นตอนการพัฒนาโมเดล AI**
    - เพื่ออธิบายทฤษฎีและแนวคิดพื้นฐานเบื้องต้น Machine Learning และ Neural Network
    - เพื่อสาธิตการทำนายผลของโมเดล

    **📚 เนื้อหาภายในเว็บไซต์:**
    - **Introduction** – แนะนำอธิบายรายวิชา โครงสร้าง และวัตถุประสงค์ของการพัฒนาระบบ
    - **Machine Learning Model** – อธิบายกระบวนการและรูปแบบการทำงานของ Machine Learning
    - **Neural Network Model** – อธิบายกระบวนการและรูปแบบการทำงานของ Neural Network
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
    - ห้อง : DE-RA 
    - ชั้นปีที่ : 5
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