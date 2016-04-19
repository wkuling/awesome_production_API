"""
Simple api to serve predictions.
"""
from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
import json

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('sample_uuid',type=str)

class SimpleModel(Resource):
    """
    The resource we want to expose
    """
    def get(self):
        args = parser.parse_args()
        d = {}
        d['sample_uuid'] = args['sample_uuid']
        d['probability'] = 0.0
        d['label'] = 0
        print(d)
        return jsonify(d)

api.add_resource(SimpleModel, 'api/v1/predict/')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000, debug=True)
