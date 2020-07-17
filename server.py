import os
import json
import glob
import pickle
import numpy as np
from PIL import Image
from datetime import datetime
# from urllib.request import urlopen
from feature_extractor import FeatureExtractor
from flask import Flask, request, render_template, jsonify, abort

app = Flask(__name__)

# Read image features
feature_extractor = FeatureExtractor()

features = []
img_paths = []
for feature_path in glob.glob("static/feature/*.pkl"):
    features.append(pickle.load(open(feature_path, 'rb+')))
    img_paths.append('static/img/' + os.path.splitext(os.path.basename(feature_path))[0] + '.jpg')

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

        try:
            print('saving image')
            uploaded_img_path = "static/uploaded/" + datetime.now().isoformat() + "_" + file.filename
            uploaded_img.save(uploaded_img_path)
        except Exception as e:
            print(e)
            
        print('extrating image features')
        query_img = feature_extractor.extract_img_features(uploaded_img)
        sim_distance_score = np.linalg.norm(features - query_img, axis=1)  # Do search
        img_result_indices = np.argsort(sim_distance_score)[1:30] # Top 30 results
        scores = [(sim_distance_score[img_index], img_paths[img_index]) for img_index in img_result_indices]

        scores_dict = [ { str(score[1]): str(score[0]) } for score in scores]
        return jsonify(scores_dict)

    else:
        abort('Check if you are hitting the right endpoint :)')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
