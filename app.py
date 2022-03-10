from crypt import methods
from flask import Flask, jsonify
from resources.chess import (
    Pawn,
    Knight,
    Bishop,
    Rook,
    Queen,
    King,
    flatBoard,
)

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Available paths:</br> /api/v1/<string:chessFigure>/<string:currentField></br> /api/v1/<string:chessFigure>/<string:currentField>/<string:destField></p>"


@app.route("/api/v1/<string:chessFigure>/<string:currentField>", methods=["GET"])
def available_figure_moves(chessFigure: str, currentField: str) -> object:
    currentField = currentField[0].upper() + currentField[1:]
    chessFigure = chessFigure.lower()
    figures = {
        "pawn": Pawn(currentField),
        "knight": Knight(currentField),
        "bishop": Bishop(currentField),
        "rook": Rook(currentField),
        "queen": Queen(currentField),
        "king": King(currentField),
    }
    e = "null"

    if currentField not in flatBoard:
        e = "Field does not exist"
        return (
            jsonify(
                {
                    "availableMoves": [],
                    "error": e,
                    "figure": chessFigure,
                    "currentField": currentField,
                }
            ),
            409,
        )

    if chessFigure not in figures:
        e = "Wrong figure"
        return (
            jsonify(
                {
                    "availableMoves": [],
                    "error": e,
                    "figure": chessFigure,
                    "currentField": currentField,
                }
            ),
            404,
        )

    return (
        jsonify(
            {
                "availableMoves": figures[chessFigure].list_available_moves(),
                "error": e,
                "figure": chessFigure,
                "currentField": currentField,
            }
        ),
        200,
    )


@app.route(
    "/api/v1/<string:chessFigure>/<string:currentField>/<string:destField>",
    methods=["GET"],
)
def is_move_valid(chessFigure: str, currentField: str, destField: str) -> object:
    currentField = currentField[0].upper() + currentField[1:]
    chessFigure = chessFigure.lower()
    destField = destField[0].upper() + destField[1:]
    e = "null"
    figures = {
        "pawn": Pawn(currentField),
        "knight": Knight(currentField),
        "bishop": Bishop(currentField),
        "rook": Rook(currentField),
        "queen": Queen(currentField),
        "king": King(currentField),
    }

    figures[chessFigure].list_available_moves()
    isValid = figures[chessFigure].validate_move(destField)
    status = 200

    if isValid == "invalid":
        e = "Current move is not permitted"
        status = 409

    if destField not in flatBoard:
        e = "Field does not exist"
        status = 409

    if currentField == destField:
        e = "You cannot move on the same place"
        status = 409

    return (
        jsonify(
            {
                "move": isValid,
                "figure": chessFigure,
                "error": e,
                "currentField": currentField,
                "destField": destField,
            }
        ),
        status,
    )


if __name__ == "__main__":
    app.run(debug=True, port=8000)
