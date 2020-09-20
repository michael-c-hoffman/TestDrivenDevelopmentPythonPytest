import json

import pytest
from flask import Response

import flasktest


def test_defaultRoute(client):
    data = {
        "foo": "bar"
    }
    mimetype = 'application/json'
    headers = {'Content-Type': mimetype, 'Accept': mimetype}
    response = client.post('/', data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    assert response.data == bytes(json.dumps(data), 'utf-8')
