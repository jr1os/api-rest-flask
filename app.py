from flask import flask

app = flask(__name__)


@app.route("/")
def index():
    return "hello world"

@app.route("/add/<int:value1>/<int:value2>")
def add(value1, value2):
    return f"result = {value1} + {value2}"