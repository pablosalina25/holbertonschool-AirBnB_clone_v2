#!/usr/bin/python3
""" Flask Application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display "Hello HBNB!" on the homepage."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display "HBNB" on a specific route."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display "C " followed by the value of the text variable,
    with underscores replaced by spaces."""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Display "Python " followed by the value of the text variable,
    with underscores replaced by spaces."""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/python/', strict_slashes=False)
def python_cool():
    """Display "Python is cool"."""
    return "Python is cool"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
