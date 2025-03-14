import sys
import os

# make sure the modified version is imported
captcha_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, captcha_path)

from src.captcha.image import ImageCaptcha

image = ImageCaptcha(
    fonts=['/mnt/vaporeon/tmp/bakery.ttf'], 
    noise_dots_number=10, 
    noise_dots_thickness=10,
    rotation_angle=60,
    char_spacing=0.0 # between 0.0-1.0: 1.0 means no space.
    )

# TODO: "color gradient"

data = image.generate('hello')
image.write('hello', 'out.png')