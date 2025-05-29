import streamlit as st
from db import get_documents

# Password Protection
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    password = st.text_input("Enter password", type="password")
    if password == "tekhaus2025":
        st.session_state.authenticated = True
        st.experimental_rerun()
    else:
        st.error("Incorrect password")
        st.stop()
