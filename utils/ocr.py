import easyocr
import numpy as np
from PIL import Image

reader = easyocr.Reader(['en'])

def extract_text(uploaded_file):

    image = Image.open(uploaded_file)
    image = np.array(image)

    results = reader.readtext(image)

    text = ""

    for result in results:
        text += result[1] + "\n"

    return text