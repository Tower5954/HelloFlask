from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1 style='text-align: center'>Hello, World!</h1>"\
           "<p> This is a new paragraph. </p> "\
           "<img src='https://media2.giphy.com/media/j4q4h9uWKWwnYT1k3Z/100.webp?cid=ecf05e47fq10w6qwd3whvi0nuj5p26lqauunl94heax7xy23&rid=100.webp' width=800>"
@app.route("/bye")
def bye():
    return "Bye!"


@app.route("/<name>")
def greet(name):
    return f"Hello there {name}"


if __name__ == "__main__":
    app.run(debug=True)

