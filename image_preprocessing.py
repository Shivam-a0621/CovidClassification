
import tensorflow as tf



img_height = 180
img_width = 180

img_path="/content/drive/MyDrive/notcovid.jpeg"

img = tf.keras.utils.load_img(
    img_path,target_size=(img_height,img_width)
)

img_array= tf.keras.utils.img_to_array(img)
img_array=tf.expand_dims(img_array,0)


