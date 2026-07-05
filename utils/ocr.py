from PIL import Image
import pytesseract
import streamlit as st

def extract_text(uploaded_file):
    """
    Stable OCR for Streamlit Cloud (NO CRASH VERSION)
    """

    # Convert uploaded file → image
    image = Image.open(uploaded_file)

    # OCR extraction
    text = pytesseract.image_to_string(image)

    return text