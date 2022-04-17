from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
import json

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app) #comment this on deployment
api = Api(app)

@app.route("/")
def index():
    return send_from_directory(app.static_folder,'index.html')

@app.route('/hello', methods=['GET'])
def helloWorld():
    return {
        'resultStatus': 'SUCCESS',
        'message': "Hello Api Handler!"
    }

@app.route('/update', methods=['POST','DELETE'])
def updateTodo():
    parser = reqparse.RequestParser()
    parser.add_argument('type', type=str)
    parser.add_argument('message', type=str)

    args = parser.parse_args()

    print(args)

    request_type = args['type']
    request_msg = args['message']
    data = []
    # currently just returning the request straight back
    if request_type == "create":
        with open('json.json') as json_file:
            data = json.load(json_file)
            data.append({'todo':request_msg})
            with open('json.json', 'w') as outfile:
                json.dump(data, outfile)
            print(data)

    elif request_type == "delete":
        with open('json.json') as json_file:
            data = json.load(json_file)
            for key in data:
                if key['todo'] == request_msg:
                    data.remove(key)
            with open('json.json', 'w') as outfile:
                json.dump(data, outfile)
            print(data)

    
    final_ret = {"status": "Success", "message": data}

    return final_ret