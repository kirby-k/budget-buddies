import flask
from . import app, client
from .db import functions

@app.route('/')
def ping():
    return 'OK', 200

@app.route('/user', methods=['GET'])
def get_user():
    user_id = flask.request.args.get('user_id', None)
    if not user_id:
        return 'Missing user_id param', 400
    user = functions.get_user(client, user_id)
    if user:
        return user, 200
    else:
        return f'User with _id "{user_id}" does not exist', 400
    
@app.route('/user', methods=['POST'])
def add_user():
    user = flask.request.json
    res = functions.add_user(client, user)
    if res:
        return res, 200
    else:
        return f'Error creating user {user}', 400

@app.route('/budget', methods=['GET'])
def get_budget():
    budget_id = flask.request.args.get('budget_id', None)
    if not budget_id:
        return 'Missing budget_id param', 400
    budget = functions.get_budget(client, budget_id)
    if budget:
        return budget, 200
    else:
        return f'Budget with _id "{budget_id}" does not exist', 400

@app.route('/budget', methods=['POST'])
def add_budget():
    budget = flask.request.json
    user_id = flask.request.args.get('user_id', None)
    if not user_id:
        return 'Missing user_id param', 400
    res = functions.add_budget(client, user_id, budget)
    if res:
        return res, 200
    else:
        return f'Error creating budget {budget} for user {user_id}.', 400

@app.route('/budget', methods=['DELETE'])
def delete_budget():
    budget_id = flask.request.args.get('budget_id', None)
    user_id = flask.request.args.get('user_id', None)
    if not budget_id:
        return 'Missing budget_id param', 400
    if not user_id:
        return 'Missing user_id param', 400
    res = functions.delete_budget(client, user_id, budget_id)
    if res:
        return res, 200
    else:
        return f'Error deleting budget {budget_id} for user {user_id}.', 400

@app.route('/budget', methods=['PUT'])
def edit_budget():
    return 'OK', 200