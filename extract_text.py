# extract_text.py

import fitz  # PyMuPDF
import os
from docx import Document

def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()

def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().strip()

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs if para.text.strip() != ""])

def extract_text(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    ext = file_path.lower().split('.')[-1]
    
    if ext == 'pdf':
        return extract_text_from_pdf(file_path)
    elif ext == 'txt':
        return extract_text_from_txt(file_path)
    elif ext == 'docx':
        return extract_text_from_docx(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")
