
import streamlit as st
from db import get_documents

# Password Protection
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    password = st.text_input("Enter password", type="password")
    if password == "tekhaus2025":
        st.success("Access granted. Reloading...")
        st.session_state.authenticated = True
        st.stop()
    else:
        st.error("Incorrect password")
        st.stop()

# App Content
st.title("👨‍👩‍👧 Custody Timeline App")
st.write("Connected to PostgreSQL. Showing document records.")

documents = get_documents()
if documents:
    for doc in documents:
        st.write(f"📄 {doc['file_name']} - {doc['file_type']} ({doc['uploaded_at']})")
else:
    st.warning("No documents found.")
