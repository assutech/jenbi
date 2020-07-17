import os
import json
import glob
import pickle
import numpy as np
from PIL import Image
from datetime import datetime
from prediction import predict_img, save_image
# from urllib.request import urlopen
from feature_extractor import FeatureExtractor
from flask import Flask, request, render_template, jsonify, abort

app = Flask(__name__)

class RequestError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


@app.errorhandler(RequestError)
def handle_request_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

@app.route('/')
def index():
    var = "YOU'RE IN THE RIGHT PLACE"
    return render_template('index.html', var=var)
    
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            print('opening image')
            file = request.files['media']
            uploaded_img = Image.open(file.stream)  # PIL image
        except Exception as e:
            print(e)
        save_image(file)
        predictions = predict_img(uploaded_img)
        return predictions
    raise RequestError()
        

if __name__ == "__main__":
    app.run()