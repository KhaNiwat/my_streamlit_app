import tensorflow as tf
import pickle
import numpy as np

model = tf.keras.models.load_model('models/titanic_model.h5')
weights = []
for layer in model.layers:
    # Get weights if the layer has them (Dense layers have len(weights) == 2, dropout has 0)
    w = layer.get_weights()
    if len(w) > 0:
        weights.append({'W': w[0], 'b': w[1]})

print("Extracted layers:", len(weights))

with open('models/titanic_weights.pkl', 'wb') as f:
    pickle.dump(weights, f)

print("Weights saved successfully.")
