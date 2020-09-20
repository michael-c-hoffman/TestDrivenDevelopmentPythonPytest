from flask import Flask, request

from .submod import submod

app = Flask(__name__)

@app.route('/', methods=['GET'])
def defaultRouteGet():
    return submod.submod

@app.route('/', methods=['POST'])
def defaultRoutePost():
    return request.get_data()
