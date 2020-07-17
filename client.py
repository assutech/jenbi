import requests
from PIL import Image
# from urllib.request import urlopen

# url = 'https://ec2-18-177-142-76.ap-northeast-1.compute.amazonaws.com/predict'
# url = 'https://212.60.86.80/32:443/predict'
url = 'http://0.0.0.0:8080/predict'
# test_img_url = 'https://assutech.gm/images/team/hassan.jpg'
test_img_url = '/home/ibrahim/Pictures/me.jpg'


payload = {'media' : open(test_img_url, 'rb')}
data = requests.post(url, files = payload)

# print(data.status_)
print(data.content)
print(data.status_code)
