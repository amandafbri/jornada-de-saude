import base64
import streamlit as st


def reset_page_state(prefix: str):
    for key in st.session_state:
        if key.startswith(prefix):
            del st.session_state[key]


def reset_st_state():
    st.session_state.clear()


def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )
