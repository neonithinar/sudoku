import tensorflow as tf
from tensorflow import keras
import numpy as np
# import matplotlib.pyplot as plt
import os

try:
    model = keras.models.load_model("MNIST_model_99.h5")
    def predictor(image):
        prediction = model.predict(image)
        return prediction

except:
    print("model not trained and compiled")


# print(model.summary())
