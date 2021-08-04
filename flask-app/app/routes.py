import datetime
import flask
from . import app, session, cfg, redis
from .db import functions

@app.route('/')
def ping():
    return 'OK', 200