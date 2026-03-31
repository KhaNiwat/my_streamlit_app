import streamlit as st
from streamlit_option_menu import option_menu

def render_nav_bar(current_page="Home"):
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
    paths = {
        "Home": "app.py",
        "ML Heart Disease": "pages/Machine_Learning.py",
        "ML Heart Model": "pages/Machine_Learning_Models.py",
        "NN Titanic": "pages/Neural_networks.py",
        "NN Titanic Model": "pages/Neural_networks_model.py"
    }

    try:
        default_idx = pages.index(current_page)
    except ValueError:
        default_idx = 0

    selected = option_menu(
        menu_title=None,
        options=pages,
        icons=icons,
        menu_icon="cast",
        default_index=default_idx,
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

    if selected != current_page:
        st.switch_page(paths[selected])
