from flask import Flask, request, render_template, flash, redirect
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

img_height = 180
img_width = 180

app = Flask(__name__, template_folder="templates")
app.secret_key = "234nf2i34rni3rrn"
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MODEL_PATH'] = 'my_model.h5'
app.config['CLASSES'] = ['covid', 'normal', 'pneumonia']

model = tf.keras.models.load_model(app.config['MODEL_PATH'], compile=False)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        flash('File uploaded successfully')
        return redirect('/')
    
    last_file_path = None
    class_name = None
    
    if request.method == 'GET':
        uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
        if uploaded_files:
            last_file = sorted(uploaded_files, key=lambda x: os.path.getmtime(os.path.join(app.config['UPLOAD_FOLDER'], x)))[-1]
            last_file_path = os.path.join(app.config['UPLOAD_FOLDER'], last_file)
            
            img = tf.keras.utils.load_img(last_file_path, target_size=(img_height, img_width))
            img_array = tf.keras.utils.img_to_array(img)
            img_array = np.expand_dims(img_array, 0)
            
            pred = model.predict(img_array)
            score = tf.nn.softmax(pred[0])
            class_name = app.config['CLASSES'][np.argmax(score)]
    
    return render_template('index.html', last_file_path=last_file_path, class_name=class_name)


if __name__ == '__main__':
    app.run(debug=True)
