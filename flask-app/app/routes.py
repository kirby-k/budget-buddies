import datetime
import flask
from . import app
from .db import functions

@app.route('/')
def ping():
    return 'OK', 200

@app.route('/user', methods=['GET'])
def get_user():
   	# fetch the user as a json object and return it
	username = flask.request.args.get('username', None)
	password = flask.request.args.get('password', None)
	user_id = functions.get_user_id(username, password)
	if not user_id:
		return "could not get user_id from db", 400

	user = functions.get_user(user_id)
	if user:
		return user, 200
	else:
		return "could not get user from db", 400
    
@app.route('/user', methods=['POST'])
def add_user():
    # add to database and return the db generated id with 200 if successful
    # return error message with failure code
	user = flask.request.json
	user_id = functions.add_user(user)
	if user_id:
		return user_id, 200
	else:
		return "add user to db failed", 400

@app.route('/budget', methods=['GET'])
def get_budget():
	budget_id = flask.request.args.get('_id', None)
	budget = functions.get_budget(budget_id)
	if budget:
		return budget, 200
	else:
		return "could not get budget from db", 400

@app.route('/budget', methods=['POST'])
def add_budget():
	budget = flask.request.json
	budget_id = functions.add_budget(budget)
	if budget_id:
		return budget_id, 200
	else:
		return "add budget to db failed", 400

@app.route('/budget', methods=['DELETE'])
def delete_budget():
	budget_id = flask.request.args.get('_id', None)
	budget = functions.delete_budget(budget_id)
	if budget:
		return budget, 200
	else:
		return "delete budget from db failed", 400

@app.route('/budget', methods=['PUT'])
def edit_budget():
	budget_id = flask.request.args.get('_id', None)
	budget = flask.request.json
	newBudget = functions.edit_budget(budget_id, budget)
	if newBudget:
		return newBudget, 200
	else:
		return "could not edit budget in db", 400
