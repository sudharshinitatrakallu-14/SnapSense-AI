import easyocr
import streamlit as st
import numpy as np
from PIL import Image

@st.cache_resource
def get_reader():
    return easyocr.Reader(['en'], gpu=False)

def extract_text(uploaded_file):
    """
    Safe OCR for Streamlit uploaded file
    """

    reader = get_reader()

    # Convert Streamlit file → PIL Image
    image = Image.open(uploaded_file)

    # Convert PIL → numpy array (IMPORTANT FIX)
    image_np = np.array(image)

    # OCR processing
    result = reader.readtext(image_np, detail=0)

    text = " ".join(result)

    return text
