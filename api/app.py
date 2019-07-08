from flask import Flask, request, Response, send_file
from src.infer import Infer

import cv2
import numpy as np
import sys
import pickle

app = Flask(__name__)

@app.route('/infer/<key>', methods=['POST'])
def inf(key):

    payload = request.data
    infer = Infer()
    res = infer.encode_image(infer.insert_bboxes(infer.decode(payload), infer.detect_encoded(payload)))

    return Response(response=res, status=200, mimetype="image/png")