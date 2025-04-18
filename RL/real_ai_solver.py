# import keras
import tensorflow.keras as keras
import os
import cv2
import numpy as np

from utils.path_utils import get_path_from_project_root

MODEL_PATH = get_path_from_project_root("model", "keras_cifar10_trained_model_2.h5")

# os.path.join(os.getcwd(), "..", "results", "captcha1.png")
def solve(path_input_image: str):
    
    CAPTCHA_PATH = path_input_image
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
    