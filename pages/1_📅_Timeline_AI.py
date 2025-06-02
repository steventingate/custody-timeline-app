
import streamlit as st
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
DB_URL = os.environ.get("DB_URL")

def connect():
    return psycopg2.connect(DB_URL, cursor_factory=RealDictCursor)

def fetch_document_texts(limit=100):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT id, file_name, content FROM documents ORDER BY uploaded_at DESC LIMIT %s", (limit,))
        results = cur.fetchall()
        cur.close()
        conn.close()
        return results
    except Exception as e:
        st.error(f"Database error: {e}")
        return []

def extract_timeline_events(documents):
    prompt = "You are a legal assistant. Extract important custody-related events from the following documents. For each event, list the date if available, a short title, and a 1–2 sentence summary. Format it as bullet points.\n\n"
    for doc in documents:
        prompt += f"Document: {doc['file_name']}\nContent:\n{doc['content'][:2000]}\n\n"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ AI error: {e}"

st.set_page_config(page_title="Custody Timeline", layout="wide")
st.title("📅 AI Timeline View")

doc_limit = st.slider("How many recent documents to process?", 10, 200, 50)
docs = fetch_document_texts(limit=doc_limit)

if st.button("🧠 Generate Timeline"):
    with st.spinner("Asking AI to summarize events..."):
        timeline = extract_timeline_events(docs)
    st.markdown("### 📝 Extracted Events")
    st.markdown(timeline)
else:
    st.info("Click the button to generate the custody event timeline using AI.")
