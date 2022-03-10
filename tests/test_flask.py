from app import app


# /api/v1/<string:chessFigure>/<string:currentField>
# Available Moves


def test_available_moves_valid_figure_valid_field():
    response = app.test_client().get("/api/v1/Pawn/H1")

    assert response.status_code == 200
    assert response.json["availableMoves"] == ["H2"]
    assert response.json["error"] == "null"
    assert response.json["figure"] == "pawn"
    assert response.json["currentField"] == "H1"


def test_available_moves_invalid_figure_valid_field():
    response2 = app.test_client().get("/api/v1/Cat/H8")

    assert response2.status_code == 404
    assert response2.json["availableMoves"] == []
    assert response2.json["error"] == "Wrong figure"
    assert response2.json["figure"] == "cat"
    assert response2.json["currentField"] == "H8"


def test_available_moves_valid_figure_invalid_field():
    response3 = app.test_client().get("/api/v1/Queen/H15")

    assert response3.status_code == 409
    assert response3.json["availableMoves"] == []
    assert response3.json["error"] == "Field does not exist"
    assert response3.json["figure"] == "queen"
    assert response3.json["currentField"] == "H15"


def test_available_moves_valid_figure_valid_field_invalid_methods():
    response4 = app.test_client().post("/api/v1/King/D4")
    response5 = app.test_client().put("/api/v1/King/D4")
    response6 = app.test_client().delete("/api/v1/Bishop/D6")

    assert response4.status_code == 405
    assert response5.status_code == 405
    assert response6.status_code == 405


def test_available_moves_corrected_figure_valid_field():
    response7 = app.test_client().get("/api/v1/PAWn/h1")

    assert response7.status_code == 200
    assert response7.json["availableMoves"] == ["H2"]
    assert response7.json["error"] == "null"
    assert response7.json["figure"] == "pawn"
    assert response7.json["currentField"] == "H1"


def test_valid_figure_wrong_address():
    response8 = app.test_client().get("/api/v1/rook")

    assert response8.status_code == 404


# address /api/v1/<string:chessFigure>/<string:currentField>/<string:destField>
# Is Move Valid


def test_valid_move_valid_figure_valid_field():
    response = app.test_client().get("/api/v1/Rook/H1/H2")

    assert response.status_code == 200
    assert response.json["move"] == "valid"
    assert response.json["figure"] == "rook"
    assert response.json["error"] == "null"
    assert response.json["currentField"] == "H1"
    assert response.json["destField"] == "H2"


def test_invalid_move_valid_figure_wrong_field():
    response = app.test_client().get("/api/v1/Rook/H1/B2")

    assert response.status_code == 409
    assert response.json["move"] == "invalid"
    assert response.json["figure"] == "rook"
    assert response.json["error"] == "Current move is not permitted"
    assert response.json["currentField"] == "H1"
    assert response.json["destField"] == "B2"


def test_valid_move_invalid_figure():
    response3 = app.test_client().get("/api/v1/Dog/B1/B2")

    assert response3.status_code == 500


def test_invalid_move_valid_figure_not_existing_field():
    response = app.test_client().get("api/v1/Knight/A1/E10")

    assert response.status_code == 409
    assert response.json["move"] == "invalid"
    assert response.json["figure"] == "knight"
    assert response.json["error"] == "Field does not exist"
    assert response.json["currentField"] == "A1"
    assert response.json["destField"] == "E10"


def test_invalid_move_valid_figure_same_field():
    response = app.test_client().get("api/v1/Queen/D1/D1")

    assert response.status_code == 409
    assert response.json["move"] == "invalid"
    assert response.json["figure"] == "queen"
    assert response.json["error"] == "You cannot move on the same place"
    assert response.json["currentField"] == "D1"
    assert response.json["destField"] == "D1"


def test_method_not_allowed():
    response1 = app.test_client().post("api/v1/Pawn/D2/D3")
    response2 = app.test_client().put("api/v1/Pawn/D2/D3")
    response3 = app.test_client().delete("api/v1/Pawn/D2/D3")

    assert response1.status_code == 405
    assert response2.status_code == 405
    assert response3.status_code == 405


def test_valid_move_corrected_figure_valid_field():
    response = app.test_client().get("api/v1/KiNg/d1/E2")

    assert response.status_code == 200
    assert response.json["move"] == "valid"
    assert response.json["figure"] == "king"
    assert response.json["error"] == "null"
    assert response.json["currentField"] == "D1"
    assert response.json["destField"] == "E2"


def test_invalid_address():
    response = app.test_client().get("api/v1/Pawn")

    assert response.status_code == 404
