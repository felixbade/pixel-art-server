import json
import shelve
import random

from flask import Flask
from flask import request, Response
from flask_cors import CORS

from secret import port

app = Flask(__name__)
CORS(app)
db = shelve.open('pixel-art.data')

def json_response(obj):
    return Response(json.dumps(obj), mimetype='application/json')

@app.route('/')
def index():
    return json_response({'status': 'ok'})

@app.route('/sprites', methods=['POST'])
def write():
    data = request.json
    sprite = {
        #'colors'
        'graphic': data['graphic']
    }
    sprites = db.get('data', [])
    sprites.append(sprite)
    db['data'] = sprites
    return json_response({
        'status': 'ok',
    })

@app.route('/sprites', methods=['GET'])
def read():
    sprites = db.get('data', [])
    return json_response(sprites)

app.run(port=port, debug=False)
db.close()