
import hashlib
from utils.ocr import extract_text
from db import insert_document

def handle_upload(file):
    content = file.read()
    file_hash = hashlib.sha256(content).hexdigest()
    file_type = file.name.split('.')[-1].lower()
    try:
        text = extract_text(file_type, content)
        success = insert_document(file.name, file_type, file_hash, text)
        if success:
            return {"status": "success"}
        else:
            return {"status": "error", "message": "Database insert failed or duplicate file."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
