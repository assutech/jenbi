import numpy as np
from feature_extractor import FeatureExtractor
import glob
import pickle
import os
from flask import jsonify

feature_extractor = FeatureExtractor()

features = []
img_paths = []
for feature_path in glob.glob("static/feature/*.pkl"):
    features.append(pickle.load(open(feature_path, 'rb+')))
    img_paths.append('static/img/' + os.path.splitext(os.path.basename(feature_path))[0] + '.jpg')

def predict_img(uploaded_img):        
    print('extrating image features')
    query_img = feature_extractor.extract_img_features(uploaded_img)
    sim_distance_score = np.linalg.norm(features - query_img, axis=1)  # Do search
    img_result_indices = np.argsort(sim_distance_score)[1:30] # Top 30 results
    scores = [(sim_distance_score[img_index], img_paths[img_index]) for img_index in img_result_indices]

    scores_dict = [ { str(score[1]): str(score[0]) } for score in scores ]
    return jsonify(scores_dict)

def save_image(file):
    try:
        print('saving image')
        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat() + "_" + file.filename
        uploaded_img.save(uploaded_img_path)
        print('image saved!')
    except Exception as e:
        print(e)
