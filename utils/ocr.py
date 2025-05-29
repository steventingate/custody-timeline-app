
import io
import fitz  # PyMuPDF
from PIL import Image
from docx import Document
import extract_msg  # NEW for .msg support

def extract_text(file_type, content):
    if file_type == "pdf":
        text = ""
        doc = fitz.open(stream=content, filetype="pdf")
        for page in doc:
            text += page.get_text()
        return text.strip()

    elif file_type in ["jpg", "jpeg"]:
        return "[Image file uploaded — OCR not supported in current environment]"

    elif file_type == "docx":
        doc = Document(io.BytesIO(content))
        return "\n".join([p.text for p in doc.paragraphs])

    elif file_type == "msg":
        with open("/tmp/email.msg", "wb") as temp_file:
            temp_file.write(content)
        msg = extract_msg.Message("/tmp/email.msg")
        return f"Subject: {msg.subject}\nFrom: {msg.sender}\nTo: {msg.to}\nDate: {msg.date}\n\n{msg.body}"

    else:
        raise ValueError("Unsupported file type for text extraction.")
