#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Model Serving Demo

Usage:
    main.py [--host <host>] [--port <port>] [--debug]
    main.py (-h | --help)
    main.py --version

Options:
    --host <host>                     绑定的 Host [default: 0.0.0.0]
    --port <port>                     绑定的 Port [default: 9999]
    --debug                           是否开启 Debug [default: False]
    -h --help                         显示帮助
    -v --version                      显示版本

"""

from docopt import docopt

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from model_serving.resources.xxx_model_resource import XXXModelResource


app = Flask(__name__)
CORS(app)

api = Api(app)
api.add_resource(XXXModelResource, '/v1/XXXModel')


if __name__ == '__main__':
    args = docopt(__doc__, version='Model Serving Demo v1.0.0')
    app.run(host=args['--host'], port=args['--port'], debug=args['--debug'])
