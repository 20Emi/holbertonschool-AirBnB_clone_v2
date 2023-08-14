#!/usr/bin/python3
"""task 1"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def rot():
    """ script that starts a Flask web application"""
    name = "Hello HBNB!"
    return name


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
