"""
A script that starts a Flask web application
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
/python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
"""

from flask import Flask, render_template
from flask import escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    text = escape(text.replace('_', ' '))
    return f"C {text}"

@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text="is cool"):
    text = escape(text.replace('_', ' '))
    return f"Python {text}"

@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    return render_template('number_template.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
