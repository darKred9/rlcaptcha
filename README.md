# RL Captcha

## Our version of the CAPTCHA generator

- example: rlcaptcha/captcha_generator/captcha_main/tests/captcha1.py
``` python
image = ImageCaptcha(
    fonts=['/mnt/vaporeon/tmp/bakery.ttf'], 
    noise_dots_number=10, 
    noise_dots_thickness=10,
    rotation_angle=60,
    char_spacing=0.0 # between 0.0-1.0: 1.0 means no space.
    )
```

## Miscellaneous

- Do `pip install --upgrade Pillow` before using the capatcha generator.



## Reference
- AI solver: https://github.com/DrMahdiRezaei/Deep-CAPTCHA
- Original Captcha generator: https://github.com/lepture/captcha
- Free fonts: https://www.1001freefonts.com