from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/news")
def news():
    return jsonify({"message": "Welcome to the news endpoint!", "status": "ok"})


if __name__ == "__main__":
    app.run(debug=True)
