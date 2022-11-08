import os
from typing import Dict, List, Tuple, Union, Optional

from flask import Flask, request, jsonify, Response
from marshmallow import ValidationError

from models import QuerySchema
from query_builder import query_builder

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST'])
def perform_query() -> Union[List[str], Tuple[Response, int]]:

    query1: Dict[str, Optional[str]] = {
        'cmd': request.args.get('cmd1'),
        'value': request.args.get('value1')
    }
    query2: Dict[str, Optional[str]] = {
        'cmd': request.args.get('cmd2'),
        'value': request.args.get('value2')
    }
    try:
        params: List[QuerySchema] = QuerySchema(many=True).load([query1, query2])
    except ValidationError as e:
        return jsonify(e.messages), 400

    result = None
    for query in params:
        result = query_builder(
            cmd=query.cmd,
            value=query.value,
            data=result
        )

    return jsonify(result), 200


if __name__ == '__main__':
    app.run()
