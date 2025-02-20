import streamlit as st

def NavBar():
    st.set_page_config(page_title='EDA Data SUS' ,layout="wide",page_icon='👨‍🔬')
    
    with st.sidebar:
        st.page_link('streamlit_app.py', label='Home')
        st.page_link('pages/ccr_diagnosticos.py', label='CCR Diagnosticos')
        st.page_link('pages/csv_files_page.py', label='CSV Files')