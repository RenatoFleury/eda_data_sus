import streamlit as st
import pandas as pd
import requests
import os
from io import StringIO
from components.navbar import NavBar

# def load_original_data():
#     url = 'https://raw.githubusercontent.com/[username]/[repository]/main/[file].csv'
#     response = requests.get(url)
#     if response.status_code == 200:
#         return pd.read_csv(StringIO(response.text))
#     else:
#         st.error("Failed to load data from GitHub.")
#         return None
    
def main():
    
    NavBar()

    st.title('Raw CSV files')

    csv_files = sorted([file for file in os.listdir('./csv_files') if file.endswith('.csv')])
    tables = [pd.read_csv(f'./csv_files/{file}', sep=';') for file in csv_files]
    descriptions = [
        'Diagnosticos - Câncer Colorrtal',
        'Tratamentos - Câncer Colorrtal',
        'Colonoscopia',
        'Internções - Neoplasia maligna do cólon',
        'Óbitos - Neoplasia maligna do cólon',
        'Exames de Sangue Oculto nas Fezes'
    ]

    for table,file,descripion in zip(tables,csv_files,descriptions):
        with st.expander(f'{descripion}'):
            st.write(f'File: {file}')
            st.dataframe(table)
            
if __name__ == '__main__':
    main()
    