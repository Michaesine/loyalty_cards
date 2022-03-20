#!/usr/bin/python
# hieronder importeer je al je functies
# from mongodb_functions import *
import json

from bson import json_util
from flask import Flask
from flask_restful import reqparse, Api, Resource

from coolding import *

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('number')
parser.add_argument('code')


def parse_json(data):
    return json.loads(json_util.dumps(data))


class CouponUserNew(Resource):
    def post(self, name, number, code):
        register(name, number, code)
        return {'status': 'ok'}


class CouponUserName(Resource):
    def delete(self, code):
        delete(code)
        return {'status': 'ok'}


class FindRecord(Resource):
    def get(self, name):
        x = find(name)
        return parse_json(x)


class UpdateRecord(Resource):
    def put(self, option, old, new):
        update(option, old, new)
        return {'status': 'ok'}


api.add_resource(CouponUserNew, '/loyalty/new/<name>/<number>/<code>')
api.add_resource(CouponUserName, '/loyalty/delete/<code>')
api.add_resource(FindRecord, '/loyalty/find/<name>')
api.add_resource(UpdateRecord, '/loyalty/update/<option>/<old>/<new>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
