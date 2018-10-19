#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Model Serving Demo

Usage:
    main.py [-a=<A> | --host=<A>] [-p=<P> | --port=<P>] [-d | --debug]
    main.py (-h | --help)
    main.py --version

Options:
    -h --help                         显示帮助
    -v --version                      显示版本
    -a=<A> --host=<A>                 绑定的 Host [default: 0.0.0.0]
    -p=<P> --port=<P>                 绑定的 Port [default: 9999]
    -d --debug                        是否开启 Debug [default: False]

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
