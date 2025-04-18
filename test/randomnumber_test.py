import random
import string

def _random_chars(num: int) -> str:
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=num))

print(_random_chars(6))
