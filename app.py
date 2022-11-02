import os

from flask import Flask, request, jsonify
from marshmallow import ValidationError

from models import RequestParams
from query_builder import query_builder

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST'])
def perform_query():
    query_1 = {
        'cmd': request.args.get('cmd1'),
        'value': request.args.get('value1')
    }

    query_2 = {
        'cmd': request.args.get('cmd2'),
        'value': request.args.get('value2')
    }
    try:
        params = RequestParams(many=True).load(data=[query_1, query_2])
    except ValidationError as e:
        return jsonify(e.messages), 400

    result = None
    for query in params:
        result = query_builder(
            cmd=query['cmd'],
            value=query['value'],
            data=result
        )

    return jsonify(result)


if __name__ == '__main__':
    app.run()
