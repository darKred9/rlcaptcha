import random
import string

def _random_chars(num: int) -> str:
    chars = string.ascii_letters + string.digits  # 包括大小写字母和数字
    return ''.join(random.choices(chars, k=num))

print(_random_chars(6))
