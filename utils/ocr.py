import easyocr
import numpy as np
from PIL import Image

reader = None

def extract_text(uploaded_file):
    global reader

    if reader is None:
        reader = easyocr.Reader(['en'])

    image = Image.open(uploaded_file)
    image = np.array(image)

    results = reader.readtext(image)

    text = ""
    for result in results:
        text += result[1] + "\n"

    return text
