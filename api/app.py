# from flask import Flask, request, Response
import sys
from models import loaded_models
from starlette.responses import FileResponse, Response, StreamingResponse, HTMLResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.applications import Starlette
import asyncio
import uuid

import cv2
import numpy as np
import sys    

api = Starlette()
api.add_middleware(CORSMiddleware, allow_origins=['*', 'localhost', 'http://129.213.59.242', 'http://129.213.59.242/'], allow_methods=['POST', 'GET'], allow_headers=['*'])
api.debug = True

@api.route('/infer/{key}', methods=['POST'])
async def inf(request):
    key     = request.path_params['key']
    payload = await request.body()

    image   = loaded_models[key].decode(payload)
    bboxes  = loaded_models[key].detect(image)
    print (bboxes, file=sys.stderr)
    image   = loaded_models[key].insert_bboxes(image, bboxes)
    # res     = loaded_models[key].encode_image(image)
    unique_filename = str(uuid.uuid4())
    cv2.imwrite(f'files/{unique_filename}.jpg', image)

    return Response(f'{unique_filename}', status_code=200)

@api.route('/file/{id}', methods=['GET'])
async def get_image(request):
    key     = request.path_params['id']
    return FileResponse(f'files/{key}.jpg', status_code=200)