
import psycopg2
from psycopg2.extras import RealDictCursor
import streamlit as st
import os

def get_recent_documents(limit=20):
    try:
        conn = psycopg2.connect(os.environ.get("DB_URL"), cursor_factory=RealDictCursor)
        cur = conn.cursor()
        cur.execute("SELECT file_name, file_type, uploaded_at FROM documents ORDER BY uploaded_at DESC LIMIT %s", (limit,))
        docs = cur.fetchall()
        cur.close()
        conn.close()
        return docs
    except Exception as e:
        st.error(f"DB error: {e}")
        return []
