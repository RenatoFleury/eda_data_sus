import streamlit as st
from components.navbar import NavBar

def main():

    NavBar()

    st.title('Home')
    # st.title('Hello, Streamlit!')
    # st.write('This is a simple Streamlit app.')

    # # Add a slider to the app
    # x = st.slider('Select a value')
    # st.write(f'You selected {x}.')
    # print(f'You selected {x}.')

    # # Add a button to the app
    # if st.button('Click me'):
    #     st.write('You clicked the button.')
    #     print('You clicked the button.')
        
    # # Add a checkbox to the app
    # if st.checkbox('Check me out'):
    #     st.write('You checked the box.')
    #     print('You checked the box.')

    # with st.form(key='my_form'):
    #     st.write('Inside the form')
    #     st.text_input('Enter some text')
    #     st.select_slider('Select a value', options=['A', 'B', 'C'])
    #     st.selectbox('Select options', ['A', 'B', 'C'])
        
    #     st.form_submit_button('Submit')
        
    # import pandas as pd
    # import requests
    # from io import StringIO
    # import streamlit as st

    # def load_original_data():
    #     url = 'https://raw.githubusercontent.com/[username]/[repository]/main/[file].csv'
    #     response = requests.get(url)
    #     if response.status_code == 200:
    #         return pd.read_csv(StringIO(response.text))
    #     else:
    #         st.error("Failed to load data from GitHub.")
    #         return None
        
    # with st.expander('Load data'):
    #     data = "dfwefaweffe"
    #     if data is not None:
    #         st.write(data)
        
        
if __name__ == '__main__':
    main()