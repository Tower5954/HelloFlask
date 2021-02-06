from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello, World!</h1>"


@app.route("/bye")
def bye():
    return "Bye!"


@app.route("/<name>")
def greet(name):
    return f"Hello there {name}"


if __name__ == "__main__":
    app.run(debug=True)

