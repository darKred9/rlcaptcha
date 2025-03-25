# you are not supposed to modify this file.

import pytesseract
from PIL import Image

def example_solver_pil(path_input_image: str) -> str:
    image = Image.open(path_input_image)
    text = pytesseract.image_to_string(image)
    # print(f"this is the text: >{text}<")
    return 'begin>'+text+'<end'
