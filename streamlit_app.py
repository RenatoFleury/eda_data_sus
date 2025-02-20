import streamlit as st
from components.navbar import NavBar
from pages.ccr_diagnosticos import ccr_diagnosticos_first_graph

def main():

    NavBar()
    
    st.header('Exploratory Data Analysis - Data SUS')
    
    st.write('Este é um projeto de EDA utilizando a base de dados do Data SUS. O objetivo é analisar os dados de diagnósticos de câncer colorretal e a quantidade de exames realizados por região e período. Os dados utilizados estão disponíveis no site do Data SUS.')
   
    st.write('Acesse o código fonte do projeto no [GitHub](https://github.com/RenatoFleury/eda_data_sus)')
    
    st.subheader('Overview dos dados analisados')
    ccr_diagnosticos_first_graph()


if __name__ == '__main__':
    main()