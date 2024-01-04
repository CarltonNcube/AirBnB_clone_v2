#!/usr/bin/python3
"""
Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all States.

    States are sorted by name.
    """
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template("9-states.html", states=sorted_states,
                           state=None, cities=None)


@app.route("/states/<id>", strict_slashes=False)
def state_details(id):
    """Displays an HTML page with info about <id>, if it exists."""
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda state: state.name)

    state = next((s for s in sorted_states if s.id == id), None)
    cities = state.cities if state and hasattr(state, 'cities') else None

    return render_template("9-states.html", states=sorted_states,
                           state=state, cities=cities)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
