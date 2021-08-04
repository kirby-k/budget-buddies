import datetime
import flask
from . import app, session, cfg, redis
from .db import functions

@app.route('/')
def ping():
    return 'OK', 200

@app.route('/user', methods=['GET'])
def get_user():
    user_id = flask.request.args.get('user_id', None)
    if user_id:
        # fetch the user as a json object and return it
        return 'OK', 200
    else:
        return 'user_id param not provided', 400
    
@app.route('/user', methods=['POST'])
def add_user():
    user = flask.request.json
    # add to database and return the db generated id with 200 if successful
    # return error message with failure code
    return 'OK', 200

@app.route('/budget', methods=['GET'])
def get_budget():
    return 'OK', 200

@app.route('/budget', methods=['POST'])
def add_budget():
    return 'OK', 200

@app.route('/budget', methods=['DELETE'])
def delete_budget():
    return 'OK', 200

@app.route('/budget', methods=['PUT'])
def edit_budget():
    return 'OK', 200