# Super simple Nueral network from The Nature of Code Chapter 10
# Fixed Data points so its doesnt learn much after a few runs
import tensorflow as tf
import numpy as np
import keras
from keras import layers, models


data = [
    {"x": 0.99, "y": 0.02, "label": "right"},
    {"x": 0.76, "y": -0.1, "label": "right"},
    {"x": -1.0, "y": 0.12, "label": "left"},
    {"x": -0.9, "y": -0.1, "label": "left"},
    {"x": 0.02, "y": 0.98, "label": "down"},
    {"x": -0.2, "y": 0.75, "label": "down"},
    {"x": 0.01, "y": -0.9, "label": "up"},
    {"x": -0.1, "y": -0.8, "label": "up"},
]





digit_classification = models.Sequential([
    layers.Input(shape=(2,)),
    layers.Dense(8, activation='relu'),
    layers.Dense(4, activation= 'softmax')
])
digit_classification.compile(
    optimizer='adam',
    loss = 'categorical_crossentropy',
    metrics= ['accuracy']

)

# train model
labels = ["right", "left", "down", "up"]

inputs = []
outputs = []
for item in data:
    inputs.append([item['x'], item['y']])
    outputs.append(labels.index(item['label']))

x = np.array(inputs)
y = keras.utils.to_categorical(outputs, num_classes=len(labels))
digit_classification.fit(x,y, epochs= 100, batch_size= 20)