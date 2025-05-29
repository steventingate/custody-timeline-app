
import io
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from docx import Document

def extract_text(file_type, content):
    if file_type == "pdf":
        text = ""
        doc = fitz.open(stream=content, filetype="pdf")
        for page in doc:
            text += page.get_text()
        return text.strip()
    elif file_type in ["jpg", "jpeg"]:
        image = Image.open(io.BytesIO(content))
        return pytesseract.image_to_string(image)
    elif file_type == "docx":
        doc = Document(io.BytesIO(content))
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        raise ValueError("Unsupported file type for text extraction.")
