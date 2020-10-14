import tensorflow as tf
import cv2
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras import layers

from tensorflow.keras.datasets import mnist

from matplotlib import pyplot


model = keras.Sequential(
    [
        keras.Input(shape=(250, 250, 3)),
        layers.Conv2D(32, 5, strides=2, activation="relu"),
        layers.Conv2D(32, 3, activation="relu"),
        layers.MaxPool2D(3),
        layers.Conv2D(32, 3, activation="relu"),
        layers.Conv2D(32, 3, activation="relu"),
        layers.MaxPool2D(3),
        layers.Conv2D(32, 3, activation="relu"),
        layers.Conv2D(32, 3, activation="relu"),
        layers.MaxPool2D(3),
        layers.Flatten(),
        layers.Dense(10),
        layers.Dense(5, activation="softmax"),
    ]
)    

model.summary()

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train.shape)

model.compile(optimizer="adam",loss='mean_squared_error')

history = model.fit(x=x_train, y=y_train, batch_size=32 , epochs=200, validation_data=(x_test,y_test))