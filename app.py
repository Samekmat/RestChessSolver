from flask import Flask, jsonify
from abc import ABC, abstractmethod

app = Flask(__name__)


@app.route("/", methods=["GET"])
def test():
    return jsonify({0: "test"})


if __name__ == "__main__":
    app.run(debug=True)
