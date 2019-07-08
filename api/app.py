from flask import Flask, request
from infer import Infer

import redis
import pickle

app = Flask(__name__)
cache = redis.Redis(host='redis', port = 6379)

@app.route('/load', methods=['POST'])
def load(): 
    infer = Infer()
    dumped = pickle.dumps(infer)
    key = request.args.get('key')
    cache.set(key, dumped)
    return f'{key} loaded'

@app.route('/unload/<key>')
def call(key):
    infer = pickle.loads(cache.get(key))
    count = infer.increment()
    cache.set(key, pickle.dumps(infer))
    return f'Fui chamado {count} vezes'
