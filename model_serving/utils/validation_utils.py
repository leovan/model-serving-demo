#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps
from jsonschema import validate, ValidationError
from flask_restful import request


def validate_json(schema, force=False):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            json_body = request.get_json(force=force)

            if json_body is None:
                return {'message': 'No JSON object'}, 400

            try:
                validate(json_body, schema)
            except ValidationError as e:
                return {'message': e.message}, 400

            return f(*args, **kwargs)
        return wrapper
    return decorator
