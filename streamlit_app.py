
import streamlit as st
from db import get_documents, insert_document
from utils.uploader import handle_upload

st.set_page_config(page_title="Custody Timeline", layout="wide")

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
st.subheader("📤 Upload New Documents")

uploaded_file = st.file_uploader("Upload a file", type=["pdf", "msg", "docx", "jpg", "jpeg"])
if uploaded_file:
    result = handle_upload(uploaded_file)
    if result["status"] == "success":
        st.success(f"Uploaded: {uploaded_file.name}")
    else:
        st.error(result["message"])

st.markdown("---")
st.subheader("📄 Document Records")
documents = get_documents()
if documents:
    for doc in documents:
        st.write(f"📄 {doc['file_name']} - {doc['file_type']} ({doc['uploaded_at']})")
else:
    st.info("No documents found.")
