import streamlit as st
from db import get_documents

# Password gate
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

# ✅ Main App UI (after login)
st.set_page_config(page_title="Custody Timeline", layout="wide")

st.title("👨‍👩‍👧 Custody Timeline App")
st.write("Connected to PostgreSQL. Showing latest documents.")

# Load from DB
documents = get_documents()
if documents:
    for doc in documents:
        st.write(f"📄 {doc['file_name']} - {doc['file_type']} ({doc['uploaded_at']})")
else:
    st.warning("No documents found in your database.")
