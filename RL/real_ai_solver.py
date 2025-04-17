import keras
import os
import cv2
import numpy as np



MODEL_PATH = os.path.join(os.getcwd(), "keras_cifar10_trained_model_2.h5")
CAPTCHA_PATH = os.path.join(os.getcwd(), "..", "..", "train", "data", "nPbXK_a3867885-8ac0-4e57-8406-41b6de82d991.png")

# os.path.join(os.getcwd(), "..", "results", "captcha1.png")
def solve():
    solver = keras.models.load_model(MODEL_PATH)
    alphabet = list('qwertyupasdfghjkzxcvbnm23456789')
    img = cv2.imread(CAPTCHA_PATH)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (int(135/2), int(50/2)), interpolation=cv2.INTER_AREA)
    img = np.reshape(img, (img.shape[0], img.shape[1], 1))
    img = np.expand_dims(img, axis=0)
    img = img.astype("float32")
    img /= 255
    result = solver.predict(img)
    solved_captcha = ""
    for i in range(0, 5):
        solved_captcha += alphabet[np.argmax(result[i][0])]
    return solved_captcha
    
print(solve())
