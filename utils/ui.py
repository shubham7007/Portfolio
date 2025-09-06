import streamlit as st

def set_animated_background(colors=None):
    if colors is None:
        colors = ["#1e3c72", "#2a5298", "#1e3c72", "#2a5298"]
    gradient = ", ".join(colors)
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: linear-gradient(-45deg, {gradient});
            background-size: 400% 400%;
            animation: gradientBG 5s ease infinite;
            color: white;
        }}

        @keyframes gradientBG {{
            0%{{background-position:0% 50%}}
            50%{{background-position:100% 50%}}
            100%{{background-position:0% 50%}}
        }}
        </style>
    """, unsafe_allow_html=True)
