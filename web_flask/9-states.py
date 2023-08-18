#!/usr/bin/python3
"""task 8"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(excepetion):
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    state = storage.all(State).values()
    return render_template('7-states_list.html', state=state)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    # busca un objeto específico en el almacenamiento (id)
    states = storage.all(State).values()
    aux = "not"
    for state in states:
        if state.id == id:
            aux = id
            break
    return render_template('9-states.html', aux=aux, states=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
