import keras
import os
import cv2
import numpy as np



MODEL_PATH = os.path.join(os.getcwd(), "keras_cifar10_trained_model.h5")
CAPTCHA_PATH = os.path.join(os.getcwd(), "..", "..", "train", "data", "2a6tq_ebd2a399-b14b-4a6c-b9b4-bef90f534a2a.png")

# os.path.join(os.getcwd(), "..", "results", "captcha1.png")
def solve():
    solver = keras.models.load_model(MODEL_PATH)
    img = cv2.imread(CAPTCHA_PATH)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (int(135/2), int(50/2)), interpolation=cv2.INTER_AREA)
    img = np.reshape(img, (img.shape[0], img.shape[1], 1))
    img = np.expand_dims(img, axis=0)
    result = solver.predict(img)
    return result
    
print(solve())
