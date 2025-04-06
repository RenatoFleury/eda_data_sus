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

    st.title('Tabelas')

            
if __name__ == '__main__':
    main()
    