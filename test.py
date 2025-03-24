# test for utils
from utils.path_utils import get_path_from_project_root

path = get_path_from_project_root("utils", "path_utils.py")
print(path)


# test for captcha generators
from captcha_generator.captcha_main.src.captcha.image import ImageCaptcha

font_path = get_path_from_project_root("font", "Flottflott.ttf")
output_path = get_path_from_project_root("results", "captcha1.png")

image = ImageCaptcha(
    fonts=[font_path], 
    noise_dots_number=10, 
    noise_dots_thickness=10,
    rotation_angle=60,
    char_spacing=0.0 # between 0.0-1.0: 1.0 means no space.
    )

image.write('hello', output_path)


# test for basic recognization

import pytesseract
from PIL import Image

image = Image.open(output_path)
text = pytesseract.image_to_string(image)
print(f"this is the text: >{text}<")
