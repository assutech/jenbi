import glob
import os
import pickle
from PIL import Image
from tqdm import tqdm
from urllib.request import urlopen
from feature_extractor import FeatureExtractor

if __name__ == '__main__':
    feature_extractor = FeatureExtractor()
    def 
    for img_path in sorted(glob.glob('static/img/*.jpg')):
        try:
            img = Image.open(img_path)  # PIL image
        except IOError:
            raise 'image couldn\'t be opened'

        feature = feature_extractor.extract_img_features(img)
        feature_path = 'static/feature/' + os.path.splitext(os.path.basename(img_path))[0] + '.pkl'
        pickle.dump(feature, open(feature_path, 'wb'))


# def get_file_list(root_dir):
#     file_list = []
#     counter = 1
#     extensions = ['.jpg', '.JPG', '.jpeg', '.JPEG', '.png', '.PNG']
#     for root, directories, filenames in os.walk(root_dir):
#         for filename in filenames:
#             if any(ext in filename for ext in extensions):
#                 file_list.append(os.path.join(root, filename))
#                 counter += 1
#     return file_list


# root_dir = 'static/img'
# filenames = sorted(get_file_list(root_dir))

# feature_list = []
# for i in tqdm(range(len(filenames))):
#     feature_list.append(feature_extractor.extract_img_features(filenames[i]))

# pickle.dump(feature_list, open('static/feature/jenda-img-features.pickle', 'wb'))
