
import streamlit as st
from db import get_documents
from utils.uploader import handle_upload

st.set_page_config(page_title="Custody Timeline", layout="wide", initial_sidebar_state="collapsed")

# Password protection
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    password = st.text_input("Enter password", type="password")
    if password == "tekhaus2025":
        st.session_state.authenticated = True
        st.rerun()
    else:
        st.error("Incorrect password")
        st.stop()

# App UI
st.title("👨‍👩‍👧 Custody Timeline App")
st.subheader("📤 Upload Documents")

# Allow all file types (handle validation in code)
uploaded_files = st.file_uploader("Upload one or more files", type=None, accept_multiple_files=True)
if uploaded_files:
    for uploaded_file in uploaded_files:
        result = handle_upload(uploaded_file)
        if result["status"] == "success":
            st.success(f"Uploaded: {uploaded_file.name}")
        else:
            st.error(f"{uploaded_file.name}: {result['message']}")

st.markdown("---")
st.subheader("📄 Document Records")
documents = get_documents()
if documents:
    for doc in documents:
        st.write(f"📄 {doc['file_name']} - {doc['file_type']} ({doc['uploaded_at']})")
else:
    st.info("No documents found.")
