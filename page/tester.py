from __future__ import print_function
import requests
import json
import cv2
import time
import numpy as np

addr = 'http://localhost:5000'
test_url = addr + '/infer/yolo'

# prepare headers for http request
content_type = 'image/jpg'
headers = {'content-type': content_type}

img = cv2.imread('image.jpg')
shape = img.shape
_, img_encoded = cv2.imencode('.jpg', img)
nparr1 = np.fromstring(img_encoded.tostring(), dtype=np.uint8)
image_string = img_encoded.tostring()

init_time = time.time()
response = requests.post(test_url, data=img_encoded.tostring())
print (1/(time.time() - init_time))
image = response.__dict__['_content']
nparr = np.fromstring(image, dtype=np.uint8)
nparr = np.resize(nparr, shape)
img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

cv2.imwrite('result.jpg', img)
