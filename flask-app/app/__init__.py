import os
import pymongo
import certifi

# set up the db url
url = "mongodb+srv://budget-buddies:1yRbFZqqDBtKoI9U@cluster0.psssp.mongodb.net"

# initialize the MongoDB client
client = pymongo.MongoClient(url, serverSelectionTimeoutMS=5000, tlsCAFile=certifi.where())

# get the database
database = client.BudgetBuddies
# print(database.list_collection_names())

# create the flask app
from flask import Flask
app = Flask(__name__)

# run the flask app
from app import routes
app.run(host='127.0.0.1', debug=True)
