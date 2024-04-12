#!/usr/bin/python3
"""Flask Application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!' on the homepage."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Displays 'C ' followed by the value of the text variable,
    replacing underscores with spaces."""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Displays 'Python ' followed by the value of the text variable,
    replacing underscores with spaces."""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """Displays '<n> is a number' if n is an integer."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays a HTML template with a number."""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Displays HTML with a message if number is even or odd.
    If integer, shows 'Number: n is even' if even, else 'Number: n is odd'."""
    status = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, status=status)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
