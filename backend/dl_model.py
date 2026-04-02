import tensorflow as tf
import numpy as np
import os

MODEL_PATH = "model/dl_model.keras"

def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(16, activation='relu', input_shape=(10,)),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(4, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

def load_model():
    if os.path.exists(MODEL_PATH):
        return tf.keras.models.load_model(MODEL_PATH)
    return create_model()

def save_model(model):
    model.save(MODEL_PATH)

def predict(features):
    model = load_model()
    x = np.array([list(features.values())])
    pred = model.predict(x, verbose=0)
    return int(np.argmax(pred))

def train(features, label):
    model = load_model()
    x = np.array([list(features.values())])
    y = np.array([label])
    model.fit(x, y, epochs=3, verbose=0)
    save_model(model)