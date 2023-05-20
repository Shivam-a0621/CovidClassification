
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np


model = load_model("F:\datasets\covid19\CovidProject\my_model.h5",compile=False)

img_height = 180
img_width = 180

img_path="F:\datasets\covid19\CovidProject\cest.jpeg"

img = tf.keras.utils.load_img(
    img_path,target_size=(img_height,img_width))

img_array= tf.keras.utils.img_to_array(img)
img_array=tf.expand_dims(img_array,0)


predictions = model.predict(img_array)
print(predictions)
score= tf.nn.softmax(predictions[0])
class_names=['covid', 'normal', 'pneumonia']

print(f"Imgage is {class_names[np.argmax(score)]},{100*np.max(score)} ")
