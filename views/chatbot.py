import streamlit as st
import time
import json
from utils.response import response_generator
import re


# === Streamlit UI ===
st.title("💬 Portfolio Chatbot")

# init session state
if "messages" not in st.session_state:
    st.session_state.messages = []         # list of {"role": "user"/"assistant", "content": "..."}
if "context" not in st.session_state:
    st.session_state.context = {"awaiting_project_detail": False}
if "intro_shown" not in st.session_state:
    st.session_state.intro_shown = False

# --- Show welcome (only once) ---
if not st.session_state.intro_shown:
    # render inside a temporary chat_message so it has the assistant appearance
    with st.chat_message("assistant"):
        welcome_text = (
            "👋 Hi there! I'm **Shubham's Portfolio Chatbot**.\n\n"
            "I can help you explore my background — here’s what you can ask me:\n\n"
            "• 🧑‍💼 *About me* — Learn who I am and what I do.\n"
            "• 🎓 *Education* — My academic background.\n"
            "• 💻 *Skills* — The technologies and tools I use.\n"
            "• 🚀 *Projects* — The work I’ve done and built.\n"
            "• 🧠 *Experience* — My professional journey.\n\n"
            "Go ahead, ask me anything!"
        )

        placeholder = st.empty()
        acc = ""
        for w in welcome_text.split():
            acc += w + " "
            placeholder.markdown(acc)
            time.sleep(0.1)

        # Save the welcome to history and mark shown
        st.session_state.messages.append({"role": "assistant", "content": welcome_text})
        st.session_state.intro_shown = True

# --- Display stored messages (history) ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# IMPORTANT: Always render the input widget (not inside conditionals that may skip it)
user_prompt = st.chat_input("Hi, this is Shubham — how can I help?")

# If user submitted
if user_prompt:
    # append user message
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # stream assistant reply into a single placeholder
    with st.chat_message("assistant"):
        stream = response_generator(user_prompt)
        full_response = ""
        ph = st.empty()
        for chunk in stream:
            full_response += chunk
            ph.markdown(full_response)
        # after streaming done, save final response
        st.session_state.messages.append({"role": "assistant", "content": full_response})