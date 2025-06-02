
import streamlit as st
import os
from utils.db import get_recent_documents

st.set_page_config(page_title="Custody Timeline App", layout="wide")

st.title("👨‍👩‍👧 Custody Timeline App")

st.write("Welcome. Use the sidebar to navigate between pages.")

st.subheader("📄 Recently Uploaded Documents")
docs = get_recent_documents()

if docs:
    for doc in docs:
        st.markdown(f"- **{doc['file_name']}** ({doc['file_type']}) — Uploaded: `{doc['uploaded_at']}`")
else:
    st.info("No documents found in your database.")
