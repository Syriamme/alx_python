"""
Script that starts a Flask web application
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable 
(replace underscore _ symbols with a space )
"""


from flask import Flask
from flask import escape

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def display_c_text(text):
    text = escape(text.replace('_', ' '))
    return f"C {text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
