
import os
import psycopg2
from psycopg2.extras import RealDictCursor

def get_documents():
    try:
        conn = psycopg2.connect(os.environ["DATABASE_URL"], cursor_factory=RealDictCursor)
        cur = conn.cursor()
        cur.execute("SELECT id, file_name, file_type, uploaded_at FROM documents ORDER BY uploaded_at DESC LIMIT 100;")
        results = cur.fetchall()
        cur.close()
        conn.close()
        return results
    except Exception as e:
        return [{"file_name": "Error connecting to DB", "file_type": str(e), "uploaded_at": ""}]
