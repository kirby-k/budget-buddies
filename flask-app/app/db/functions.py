'''
Defines required database queries.
'''
from bson.json_util import dumps
import pymongo
from bson.objectid import ObjectId

def get_user_by_user_pwd(client: pymongo.MongoClient, username: str, password: str) -> dict:
    '''
    Retrieves the user corresponding to a username/password combo.
    Returns None if the username doesn't exist or the password is incorrect.

    Parameters
    ----------
    client (pymongo.MongoClient) : the MongoDB client.
    username (str) : the user's username.
    password (str) : the user's password.
    ''' 
    return client.BudgetBuddies.User.find_one({
        'username': username,
        'password': password
    })

def get_user(client: pymongo.MongoClient, user_id: str) -> dict:
    '''
    Retrieves the user record corresponding to the given user_id as a json object.
    Returns None if the user_id does not exist.

    Parameters
    ----------
    client (pymongo.MongoClient) : the MongoDB client.
    user_id (str) : the _id field for the user (assuming the user exists).
    '''
    return client.BudgetBuddies.User.find_one({
        '_id': ObjectId(user_id)
    })

def add_user(client: pymongo.MongoClient, user: dict) -> str:
    '''
    Adds a new user to the database.
    Returns None if the user_id does not exist.
    Otherwise, returns the generated _id field.

    Parameters
    ----------
    client (pymongo.MongoClient) : the MongoDB client.
    user (dict) : the user json object.
    '''
    res = client.BudgetBuddies.User.insert_one(user)
    if not res.acknowledged:
        return None
    return res.inserted_id

def get_budget(client: pymongo.MongoClient, budget_id: str) -> dict:
    '''
    Retrieves the budget record corresponding to the given budget_id as a json object.
    Returns None if the budget_id does not exist.

    Parameters
    ----------
    client (pymongo.MongoClient) : the MongoDB client.
    budget_id (str) : the _id field for the budget (assuming the budget exists).
    '''
    return dumps(client.BudgetBuddies.Budget.find_one({
        '_id': ObjectId(budget_id)
    }))

def add_budget(client: pymongo.MongoClient, budget: dict) -> dict:
    '''
    Adds a new budget to the database.
    Returns None if the budget_id does not exist.
    Otherwise, returns the generated _id field.

    Parameters
    ----------
    client (pymongo.MongoClient) : the MongoDB client.
    budget (dict) : the budget json object.
    '''
    res = client.BudgetBuddies.Budget.insert_one(budget)
    if not res.acknowledged:
        return None
    return res.inserted_id

def delete_budget(budget_id: int) -> dict:
    '''
    Removes record corresponding to the given budget_id as a json object.
    Returns None if the budget_id does not exist.
    Returns the deleted _id if the budget exists.

    Parameters
    ----------
    budget_id (int) : the _id field for the budget (assuming the budget exists).
    '''
    return None

def edit_budget(budget_id: int, budget: dict) -> dict:
    '''
    Edits the budget with _id budget_id with the fields in the budget json.
    Returns None if the budget_id does not exist.
    Otherwise, returns the updated json object for the budget.

    Parameters
    ----------
    budget_id (int) : the _id field for the budget (assuming the budget exists).
    budget (dict) : the budget json object containing fields to be updated.
    '''
    return None