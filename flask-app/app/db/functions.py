'''
Defines required database queries.
'''
from html.entities import name2codepoint
import pymongo

def get_user_id(username: str, password: str) -> int:
    '''
    Retrieves the user_id corresponding to a username.
    Returns None if the username doesn't exist or the password is incorrect.

    Parameters
    ----------
    username (str) : the user's username.
    password (str) : the user's password.
    ''' 
    return None

def get_user(user_id: int) -> dict:
    '''
    Retrieves the user record corresponding to the given user_id as a json object.
    Returns None if the user_id does not exist.

    Parameters
    ----------
    user_id (int) : the _id field for the user (assuming the user exists).
    '''
    return None

def add_user(user: dict) -> dict:
    '''
    Adds a new user to the database.
    Returns None if the user_id does not exist.
    Otherwise, returns the generated _id field.

    Parameters
    ----------
    user (dict) : the user json object.
    '''
    return None

def get_budget(budget_id: int) -> dict:
    '''
    Retrieves the budget record corresponding to the given budget_id as a json object.
    Returns None if the budget_id does not exist.

    Parameters
    ----------
    budget_id (int) : the _id field for the budget (assuming the budget exists).
    '''
    return None

def add_budget(budget: dict) -> dict:
    '''
    Adds a new budget to the database.
    Returns None if the budget_id does not exist.
    Otherwise, returns the generated _id field.

    Parameters
    ----------
    budget (dict) : the budget json object.
    '''
    return None

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