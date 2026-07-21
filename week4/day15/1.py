import streamlit as st
import time 
import datetime 
from DBHELPER2 import DBHelper

#page format 
st.set_page_config(page_title='Agentic AI chatbot')
st.subheader('Write task to delegate: ')

#initializing Data Base operations 
db_helper = DBHelper()
db_helper.select_collection(collection_name='Tasks')


#hard coding some of the messages 
task_clues = {
    'How to create a task?':'Create task : title, descryption, action, contact_name, contact_phone',
    'How to view tasks?': 'list all tasks',
    'How to update task?': 'Update task : title, descryption, action, contact_name, contact_phone',
    'How to delete task?' : 'Delete task : title, descryption, action, contact_name, contact_phone'
}


#creating a list called messages in the following way because this will not delete/ over write the data of one session when the next one begins 
if 'messages' not in st.session_state:
    st.session_state.messages = []

#this lists all the previous text messages in the list messages. 
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['text'])


#taking input of message from the user 

user_input = st.chat_input('Type task here--')


if user_input:

    message = {
        'role': 'user',
        'text': user_input
    }

    st.session_state.messages.append(message)

    with st.chat_message(message['role']):
        st.markdown(message['text'])

    if user_input in task_clues:
        clue = task_clues[user_input]

        message = {
            'role': 'assistant',
            'text': clue
        }
        st.session_state.messages.append(message)

        with st.chat_message(message['role']):
            typing_placeholder = st.empty()
            typing_text = ''
            for character in message['text']:
                typing_text += character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.01)

    else:

        message = {
            'role': 'assistant',
            'text': 'Sorry, I cannot Help You'
        }
        st.session_state.messages.append(message)

        with st.chat_message(message['role']):
            typing_placeholder = st.empty()
            typing_text = ''
            for character in message['text']:
                typing_text += character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.05)