from http import HTTPStatus

import pytest

import chalicedemo


def test_index(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json == {'hello': 'world'}

@pytest.mark.parametrize("city,state", [("Portland", "OR"), ("Seattle", "WA")])
def test_CityToStatePortland(client, city, state):
    response = client.get("/locations/{city}".format(city=city))
    assert response.status_code == HTTPStatus.OK
    assert response.json == { "State": state }

@pytest.mark.parametrize("city,state", [("Cincinnati", "OH"), ("Dallas", "TX")])
def test_CityToStateNotFound(client, city, state):
    response = client.get("/locations/{city}".format(city=city))
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json == {
        "Code": "BadRequestError",
        "Message": "BadRequestError: Unknown city '{}'".format(city)
    }

@pytest.mark.parametrize("value", ["foo", "bar"])
def test_ResourcePost(client, value):
    response = client.put("/resource/{}".format(value))
    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        "value": value
    }
