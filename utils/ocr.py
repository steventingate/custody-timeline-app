import io
import fitz  # PyMuPDF
from PIL import Image
from docx import Document

def extract_text(file_type, content):
    if file_type == "pdf":
        # Extract text from PDF using PyMuPDF
        text = ""
        doc = fitz.open(stream=content, filetype="pdf")
        for page in doc:
            text += page.get_text()
        return text.strip()

    elif file_type in ["jpg", "jpeg"]:
        # Placeholder: OCR not available in Render (no Tesseract installed)
        return "[Image file uploaded — OCR not supported in current environment]"

    elif file_type == "docx":
        # Extract text from DOCX
        doc = Document(io.BytesIO(content))
        return "\\n".join([p.text for p in doc.paragraphs])

    else:
        raise ValueError("Unsupported file type for text extraction.")
