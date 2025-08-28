import streamlit as st

def NavBar():
    st.set_page_config(page_title='EDA Data SUS' ,layout="wide",page_icon='👨‍🔬')
    
    with st.sidebar:
        st.title('Menu')
        st.page_link('streamlit_app.py', label='Home')
        st.header('Analysis')
        st.page_link('pages/ccr_diagnosticos_page.py', label='CCR Diagnosticos')
        st.page_link('pages/sangue_oculto_page.py', label='Sangue Oculto')
        st.page_link('pages/ccr_internacoes_page.py', label='Internações')
        st.page_link('pages/obitos_page.py', label='Óbitos')
        st.page_link('pages/colonoscopia_page.py', label='Colonoscopia')
        
        st.divider()
        st.page_link('pages/tables_page.py', label='Tabelas')
        
        st.divider()
        st.page_link('pages/csv_files_page.py', label='Arquivos CSV')
        