#!/usr/bin/python3
"""task 1"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def rot():
    """/: display “Hello HBNB!” """
    name = "Hello HBNB!"
    return name


@app.route('/hbnb', strict_slashes=False)
def rot1():
    """/hbnb: display “HBNB”"""
    name1 = "HBNB"
    return name1


@app.route('/c/<text>', strict_slashes=False)
def rot2(text):
    text = text.replace('_', ' ')
    return f'C {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
