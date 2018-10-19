#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restful import Resource, request

from ..models.xxx_model import XXXModel
from ..utils.validation_utils import validate_json


xxx_model_instance = XXXModel()
xxx_model_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'}
    },
    'required': ['name']
}


class XXXModelResource(Resource):
    @validate_json(xxx_model_schema)
    def post(self):
        json = request.json

        return {'result': xxx_model_instance.hello(json['name'])}
