# Jenbi: Deep Learning-based Reverse Image Search Engine

## Overview
- *Jenbi* is a simple image-based image search engine using Keras + Flask. You can launch the search engine just by running two python scripts.
- `offline.py`: This script extracts deep features from images. Given a set of database images, a 4096D fc1-feature is extracted for each image using the VGG16 network with ImageNet pre-trained weights.
- `server.py`: This script runs a web-server. You can send your query image to the server via a Flask web-intereface/http post request. Then relevant images to the query are retrieved by the simple nearest neighbor search.


## Usage
```bash
# Clone the code and install libraries
$ git clone .........
$ cd jenda-sis
$ pip install -r requirements.txt

# Put your image files (*.jpg) on static/img


$ python offline.py
# Then fc1 features are extracted and saved on static/feature
# Note that it takes time for the first time because Keras downloads the VGG weights.

$ python app.py
# Now you can do the search via localhost:5000

$ python client.py
# To send a http post request to app.py
# Which yields url of images similar to the given image