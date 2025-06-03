
import streamlit as st
import os
import psycopg2
from psycopg2.extras import RealDictCursor

DB_URL = os.environ.get("DB_URL")

def connect():
    return psycopg2.connect(DB_URL, cursor_factory=RealDictCursor)

def fetch_documents(limit=100):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            SELECT id, file_name, file_type,
                   COALESCE(received_at, uploaded_at) AS event_date,
                   source, content
            FROM documents
            ORDER BY event_date DESC
            LIMIT %s
        """, (limit,))
        results = cur.fetchall()
        cur.close()
        conn.close()
        return results
    except Exception as e:
        st.error(f"Database error: {e}")
        return []

st.set_page_config(page_title="Custody Timeline Metadata", layout="wide")
st.title("📂 Timeline by Received Date")

doc_limit = st.slider("How many recent documents to show?", 10, 500, 100)
docs = fetch_documents(limit=doc_limit)

if docs:
    for doc in docs:
        with st.expander(f"📄 {doc['file_name']} — {doc['event_date'].strftime('%Y-%m-%d')}"):
            st.markdown(f"**File Type**: {doc['file_type']}")
            st.markdown(f"**Source**: {doc['source'] or 'Unknown'}")
            st.markdown(f"**Preview**: {doc['content'][:500]}...")
else:
    st.info("No documents found.")
