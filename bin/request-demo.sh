#!/usr/bin/env bash

host=0.0.0.0
port=9999
url=/v1/XXXModel
curl_url=http://${host}:${port}${url}

invalid_json='{}'
valid_json='{"name": "Leo"}'

# No JSON object
curl --request POST --url ${curl_url} --verbose

# Invalid JSON object
curl --header 'contentType: application/json; charset=UTF-8' --request POST --data ${invalid_json} --url ${curl_url} --verbose

# Valid JSON object
curl --header 'contentType: application/json; charset=UTF-8' --request POST --data ${valid_json} --url ${curl_url} --verbose