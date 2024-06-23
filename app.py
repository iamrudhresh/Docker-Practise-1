from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def say_hello():
    return "Hello, World!"


if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", debug=True)