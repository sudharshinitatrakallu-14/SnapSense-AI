import easyocr
import streamlit as st

# Load OCR model only once (VERY IMPORTANT for Streamlit)
@st.cache_resource
def get_reader():
    return easyocr.Reader(['en'], gpu=False)

def extract_text(image):
    """
    Extract text from uploaded image using EasyOCR
    """
    reader = get_reader()

    # EasyOCR accepts file-like objects or numpy arrays
    result = reader.readtext(image, detail=0)

    # Join all detected text
    text = " ".join(result)

    return text
