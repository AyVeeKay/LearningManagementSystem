from flask import Flask
from application import config


app = Flask(__name__)
app.config.from_pyfile('config.py')
