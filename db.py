
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime

def connect():
    return psycopg2.connect(os.environ["DATABASE_URL"], cursor_factory=RealDictCursor)

def get_documents():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT id, file_name, file_type, uploaded_at FROM documents ORDER BY uploaded_at DESC LIMIT 100;")
        results = cur.fetchall()
        cur.close()
        conn.close()
        return results
    except Exception as e:
        return [{"file_name": "DB Error", "file_type": str(e), "uploaded_at": ""}]

def insert_document(file_name, file_type, file_hash, content):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO documents (file_name, file_type, file_hash, content)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (file_hash) DO NOTHING;
        """, (file_name, file_type, file_hash, content))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Exception as e:
        return False
