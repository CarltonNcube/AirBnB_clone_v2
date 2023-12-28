#!/usr/bin/python3
"""
This script starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """Route that displays a HTML page with a list of States."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<string:id>', strict_slashes=False)
def state_cities(id):
    """Route that displays a HTML page with a list of Cities for a State."""
    state = storage.get(State, id)

    if state:
        return render_template('9-states_cities.html', state=state)
    else:
        return render_template('9-not_found.html')


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

