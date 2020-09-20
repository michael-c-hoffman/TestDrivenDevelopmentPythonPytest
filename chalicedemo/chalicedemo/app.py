from chalice import BadRequestError, Chalice
from chalicelib.locations.city_state import CITIES_TO_STATES

app = Chalice(app_name='chalicedemo')
# app.debug = True

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/locations/{city}')
def stateOfCity(city):
    try:
        return {"State": CITIES_TO_STATES[city]}
    except KeyError as error:
        raise BadRequestError("Unknown city '{}'".format(city))

@app.route('/resource/{value}', methods=['PUT'])
def put_test(value):
    return {"value": value}

@app.route('/introspect')
def introspect():
    return app.current_request.to_dict()
# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
