import easyocr
import streamlit as st

@st.cache_resource
def get_reader():
    return easyocr.Reader(['en'], gpu=False)

def extract_text(image):
    reader = get_reader()
    result = reader.readtext(image, detail=0)
    text = " ".join(result)
    return text
