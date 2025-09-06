import random
import time

import streamlit as st


# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hey there! Need help? Check out my fun YouTube channel 'CodingIsFun': https://youtube.com/@codingisfun!",

        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.1)


st.title("Chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Hi this is Shubham how can i help"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})