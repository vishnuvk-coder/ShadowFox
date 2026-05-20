import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Load model
model = tf.keras.models.load_model("image_model.h5")

# Class names
class_names = ['car', 'cat', 'dog']

# Image path
img_path = "car image.jpg"

# Load image
img = image.load_img(img_path, target_size=(128, 128))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)

# Predict
prediction = model.predict(img_array)

predicted_class = class_names[np.argmax(prediction)]

print("Predicted Image:", predicted_class)