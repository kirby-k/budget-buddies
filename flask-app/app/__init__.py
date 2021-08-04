import os
from app import cfg

# initialize the configuration file parser
config = cfg.initialize_cfg('<insert path here>')

# select int, test, qa, or prod environment
config_field = 'TEST'

# create the flask app
from flask import Flask
app = Flask(__name__)

# run the flask app
from app import routes
app.run(host='127.0.0.1', debug=True)


