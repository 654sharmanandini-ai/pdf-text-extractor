from pdf_text import extract_text_from_pdf
from pdf_ocr import extract_text_from_images

def extract_all_text(pdf_path: str) -> str:
    text_from_pdf = extract_text_from_pdf(pdf_path)
    text_from_images = extract_text_from_images(pdf_path)
    return text_from_pdf + "\n" + text_from_images
