import tensorflow as tf
from tensorflow import keras
import numpy as np
# import matplotlib.pyplot as plt
# import os

def train_model(train = False):
    if train == True:
        (X_train_full, y_train_full), (X_test, y_test) = keras.datasets.mnist.load_data()
        X_train_full = X_train_full / 255.

        X_test = X_test / 255.
        X_train, X_valid = X_train_full[:-5000], X_train_full[-5000:]
        y_train, y_valid = y_train_full[:-5000], y_train_full[-5000:]

        X_train = X_train[..., np.newaxis]
        X_valid = X_valid[..., np.newaxis]
        X_test = X_test[..., np.newaxis]

        datagen = keras.preprocessing.image.ImageDataGenerator(
            rotation_range = 20, width_shift_range = 0.2, height_shift_range = 0.2,
            shear_range = 0.1, zoom_range = 0.2)

        keras.backend.clear_session()
        tf.random.set_seed(42)
        np.random.seed(42)

        model = keras.models.Sequential([
            keras.layers.Conv2D(32, kernel_size=3, padding="same", activation="relu"),
            keras.layers.Conv2D(64, kernel_size=3, padding="same", activation="relu"),
            keras.layers.MaxPool2D(),
            keras.layers.Flatten(),
            keras.layers.Dropout(0.25),
            keras.layers.Dense(128, activation="relu"),
            keras.layers.Dropout(0.5),
            keras.layers.Dense(10, activation="softmax")
        ])
        model.compile(loss="sparse_categorical_crossentropy", optimizer="nadam",
                      metrics=["accuracy"])

        model.fit(X_train, y_train, epochs=10, validation_data=(X_valid, y_valid))
        model.evaluate(X_test, y_test)

        model.save("MNIST.h5")



def predict_cell(image):
    # img_array = np.mean(image, axis = 2)
    img_array = np.reshape(image, (1, 28, 28, 1))
    try:
        model = keras.models.load_model("MNIST.h5")
        predictions = model.predict(img_array)

    except:
        print("Digit recogniser model not found! \n Training the model ......")
        train_model(train= True)

    return predictions



