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

## How to run

``` bash
docker build -t captchaAI-gpu .
./rundocker.sh 
```

- mounting point: current dir -> `/workplace` in docker


## RL model

- Number of characters: 6 (fixed)
- What characters: random

- action space: 
    - noise_dots_number: [0, 100]
    - noise_dots_thickness: [1, 30]
    - rotation_angle: [-60, 60]
    - char_spacing:  [0.0, 1.0]






## Reference
- AI solver: https://github.com/DrMahdiRezaei/Deep-CAPTCHA
- Original Captcha generator: https://github.com/lepture/captcha
- Free fonts: https://www.1001freefonts.com