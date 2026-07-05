import easyocr
import streamlit as st
import numpy as np
from PIL import Image

# Load OCR model ONCE (prevents crash + restart loop)
@st.cache_resource
def get_reader():
    return easyocr.Reader(['en'], gpu=False)

def extract_text(uploaded_file):
    """
    Safe OCR for Streamlit Cloud
    """

    reader = get_reader()

    # Convert Streamlit file -> image
    image = Image.open(uploaded_file)

    # Convert PIL -> numpy (required for EasyOCR)
    image_np = np.array(image)

    # OCR
    result = reader.readtext(image_np, detail=0)

    # Join text safely
    text = " ".join(result)

    return text