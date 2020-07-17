from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
import numpy as np


class FeatureExtractor:
    def __init__(self):
        # base_model = VGG16(weights='/home/ibrahim/Desktop/vgg16_weights_tf_dim_ordering_tf_kernels.h5') # use locally
        base_model = VGG16(weights='imagenet') 
        self.model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc1').output)

    def extract_img_features(self, img):  # img is from PIL.Image.open(path) or keras.preprocessing.image.load_img(path)
        input_shape = (224, 224, 3)
        img = image.load_img(img, target_size = (input_shape[0], input_shape[1]))
        colored_img = img.convert('RGB')  # Make sure img is color
        img_array = image.img_to_array(colored_img)  # To np.array. Height x Width x Channel. dtype=float32
        expanded_img_array = np.expand_dims(img_array, axis=0)  # (H, W, C)->(1, H, W, C), where the first elem is the number of img
        preprocessed_img = preprocess_input(expanded_img_array)  # Subtracting avg values for each pixel
        features = self.model.predict(x)[0]  # (1, 4096) -> (4096, )
        normalized_features = features / np.linalg.norm(features)  # Normalize
        return normalized_features