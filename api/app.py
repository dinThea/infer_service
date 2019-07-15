# from flask import Flask, request, Response
import sys
from models import loaded_models
from starlette.responses import Response, StreamingResponse, HTMLResponse
from starlette.applications import Starlette
import asyncio

import cv2
import numpy as np
import sys    

api = Starlette()
api.debug = True

@api.route('/infer/{key}', methods=['POST', 'GET', 'OPTIONS'])
async def inf(request):
    if (request.method == 'POST'):
        key     = request.path_params['key']
        payload = await request.body() 

        image   = loaded_models[key].decode(payload)
        bboxes  = loaded_models[key].detect(image)
        image   = loaded_models[key].insert_bboxes(image, bboxes)
        res     = loaded_models[key].encode_image(image)

        return Response(res, status_code=200)
    else:
        return Response('CORS', status_code=200)


# async def slow_numbers(minimum, maximum):
#     yield('<html><body><ul>')
#     for number in range(minimum, maximum + 1):
#         yield '<li>%d</li>' % number
#         await asyncio.sleep(0.5)
#     yield('</ul></body></html>')

# @api.route('/infer/{key}/stream/{video}', methods=['GET', 'OPTIONS'])
# async def inf(request):
#     if (request.method == 'GET'):
#         response = StreamingResponse(video, media_type='text/html')
#         await response(scope, receive, send)
#     else:
#         return Response('CORS', status_code=200)