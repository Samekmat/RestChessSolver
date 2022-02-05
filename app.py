from flask import Flask, jsonify
from abc import ABC, abstractmethod

app = Flask(__name__)


@app.route("/", methods=["GET"])
def test():
    return jsonify({0: "test"})


class Figure(ABC):
    def __init__(self, position):
        self.currentField = position
        

        
if __name__ == "__main__":
    app.run(debug=True)
