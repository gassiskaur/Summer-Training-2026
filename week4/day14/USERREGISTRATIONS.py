import streamlit as st
from USERCLASS1 import *
from DBHELPER1 import *



st.title('User registration')

name= st.text_input('Enter full name:')
phone= st.text_input('Enter your phone number: ')
email= st.text_input('Enter your email: ')
password = st.text_input('Enter the password to yourr account: ')

if st.button('Register'):

    user = User(name, phone, email, password)
    document_to_save = user.to_dictionary()

    db_helper = DBHelper()
    db_helper.select_collection()
    db_helper.save(document_to_save)

    # print('User Registered')
    # print(f'{name}, {phone}, {email}, {password}')