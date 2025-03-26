from utils.path_utils import get_path_from_project_root
from captcha_generator.captcha_main.src.captcha.image import ImageCaptcha

import random
import string

font_path = get_path_from_project_root("font", "Montserrat-Regular.ttf")
output_path = get_path_from_project_root("results", "captcha1.png")

def _random_chars(num: int) -> str:
    """
    Generate a random string of the given length composed of letters and digits.

    Args:
        num (int): The desired length of the random string.

    Returns:
        str: A random string of length `num` containing letters and digits.
    """
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=num))


def env(noise_dots_number: int, noise_dot_thickness: int, rotation_angle: float, char_sapcing: float) -> str:
    """
    Generate a Captcha based on the given inputs. Save the result png file to 'results/captcha1.png'

    The CAPTCHA has a fixed length of 6 characters with randomly generated content (alphanumerical).

    Args:
        noise_dots_number: [0, 100]
        noise_dots_thickness: [1, 30]
        rotation_angle: [-60, 60]
        char_spacing:  [0.0, 1.0]
        
    Returns:
        str: The string of this Captcha
    """
    image = ImageCaptcha(
        fonts=[font_path], 
        noise_dots_number=noise_dots_number, 
        noise_dots_thickness=noise_dot_thickness,
        rotation_angle=rotation_angle, # random between (-10, 10)
        char_spacing=char_sapcing # between 0.0-1.0: 1.0 means no space.
        )

    text = _random_chars(6)

    image.write(text, output_path)

    return text