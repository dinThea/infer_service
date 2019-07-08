from __future__ import print_function
import requests
import json
import cv2
import time
import numpy as np

addr = 'http://iagoeli.pagekite.me'
test_url = addr + '/infer/yolo'

# prepare headers for http request
content_type = 'image/png'
headers = {'content-type': content_type}

img = cv2.imread('image.png')

_, img_encoded = cv2.imencode('.png', img)
# send http request with image and receive response
init_time = time.time()
response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
print (f'Duration: {1/(time.time() - init_time)}')
# decode response
image = response.__dict__['_content']

nparr = np.frombuffer(image, dtype=np.uint8)
img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

cv2.imwrite('result.png', img)
