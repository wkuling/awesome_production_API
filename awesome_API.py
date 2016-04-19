"""
Simple api to serve predictions.
"""
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import json

app = Flask(__name__)
api = Api(app)


class SimpleModel(Resource):
    """
    The resource we want to expose
    """
    def get(self):
        return 0

api.add_resource(SimpleModel, '/predict/')

if __name__ == '__main__':
     app.run(host="0.0.0.0",port=5000, debug=True)