#!/usr/bin/python3
"""task 8"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(excepetion):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def lista():
    state = storage.all(State).values()
    return render_template('8-cities_by_states.html', state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
