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

data = image.generate('hello')
image.write('hello', output_path)


# test for basic recognization

import keras_ocr

pipeline = keras_ocr.pipeline.Pipeline()
images = [keras_ocr.tools.read(output_path)]
prediction_groups = pipeline.recognize(images)

for text, box in prediction_groups[0]:
    print(text)

