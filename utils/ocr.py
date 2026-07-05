from PIL import Image
import pytesseract

def extract_text(uploaded_file):
    """
    Stable OCR for Streamlit Cloud (no crashes)
    """

    image = Image.open(uploaded_file)

    text = pytesseract.image_to_string(image)

    return text