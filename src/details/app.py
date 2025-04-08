import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

@app.route('/<name>')
def hello(name):
    return f'Alex says: hello {name}'

@app.route('/check_file/<file_name>')
def check_file(file_name):
    try:
        with open(file_name) as FILE:
            data=FILE.readline()
        return data
    except FileNotFoundError:
        return f'[!] no such file {file_name} Found'