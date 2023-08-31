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
