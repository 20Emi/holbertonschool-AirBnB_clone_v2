#!/usr/bin/python3
"""task 4"""
from flask import Flask, render_template

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


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def rot3(text="is cool"):
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def rot4(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def rot5(n):
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def rot6(n):
    if n % 2 == 0:
        res = 'even'
    else:
        res = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, res=res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
