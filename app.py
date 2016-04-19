"""
Simple api to serve predictions.
"""
from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
import json

app = Flask(__name__)
api = Api(app)


class SimpleModel(Resource):
    """
    The resource we want to expose
    """
    def get(self):
		d = {}
		d['sample_uuid'] = 'string'
		d['probability'] = 0.0
		d['label'] = 0
        return jsonify(d)

api.add_resource(SimpleModel, 'api/v1/predict/')

if __name__ == '__main__':
     app.run(host="0.0.0.0",port=5000, debug=True)
