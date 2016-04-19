"""
Simple api to serve predictions.
"""
from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
import json

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('age',type=int)
parser.add_argument('job',type=str)
parser.add_argument('marital',type=str)
parser.add_argument('education',type=str)
parser.add_argument('default',type=str)
parser.add_argument('housing',type=str)
parser.add_argument('loan',type=str)
parser.add_argument('contact',type=str)
parser.add_argument('month',type=str)
parser.add_argument('day_of_week',type=str)
parser.add_argument('duration',type=int)
parser.add_argument('campaign',type=int)
parser.add_argument('pdays',type=int)
parser.add_argument('previous',type=int)
parser.add_argument('poutcome',type=str)
parser.add_argument('emp.var.rate',type=float)
parser.add_argument('cons.price.idx',type=float)
parser.add_argument('cons.conf.idx',type=float)
parser.add_argument('euribor3m',type=float)
parser.add_argument('nr.employed',type=float)
parser.add_argument('sample_uuid',type=str)


class SimpleModel(Resource):
    """
    The resource we want to expose
    """
    def get(self):
        args = parser.parse_args()
        result = {}
        result['sample_uuid'] = args['sample_uuid']
        result['probability'] = 0.0
        result['label'] = 0
        return jsonify(result)

api.add_resource(SimpleModel, '/api/v1/predict/')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000, debug=True)
