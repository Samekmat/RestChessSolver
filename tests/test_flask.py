from app import app


def test_available_moves():
    # /api/v1/<string:chessFigure>/<string:currentField>

    response = app.test_client().get("/api/v1/Pawn/H1")
    response2 = app.test_client().get("/api/v1/Cat/H8")
    response3 = app.test_client().get("/api/v1/Queen/H15")
    response4 = app.test_client().post("/api/v1/King/D4")
    response5 = app.test_client().put("/api/v1/King/D4")
    response6 = app.test_client().delete("/api/v1/Bishop/D6")
    response7 = app.test_client().get("/api/v1/PAWn/h1")

    assert response.status_code == 200
    assert response.json["availableMoves"] == ["H2"]
    assert response.json["error"] == "null"
    assert response.json["figure"] == "pawn"
    assert response.json["currentField"] == "H1"

    assert response2.status_code == 404
    assert response2.json["availableMoves"] == []
    assert response2.json["error"] == "Wrong figure"
    assert response2.json["figure"] == "cat"
    assert response2.json["currentField"] == "H8"

    assert response3.status_code == 409
    assert response3.json["availableMoves"] == []
    assert response3.json["error"] == "Field does not exist"
    assert response3.json["figure"] == "queen"
    assert response3.json["currentField"] == "H15"

    assert response4.status_code == 405
    assert response5.status_code == 405
    assert response6.status_code == 405

    assert response7.status_code == 200
    assert response7.json["availableMoves"] == ["H2"]
    assert response7.json["error"] == "null"
    assert response7.json["figure"] == "pawn"
    assert response7.json["currentField"] == "H1"


def test_is_move_valid():
    # address /api/v1/<string:chessFigure>/<string:currentField>/<string:destField>

    response = app.test_client().get("/api/v1/Rook/H1/H2")
    response2 = app.test_client().get("/api/v1/Rook/H1/B2")
    response3 = app.test_client().get("/api/v1/Dog/B1/B2")
    response4 = app.test_client().get("api/v1/Knight/A1/E10")
    response5 = app.test_client().get("api/v1/Queen/D1/D1")
    response6 = app.test_client().post("api/v1/Pawn/D2/D3")
    response7 = app.test_client().put("api/v1/Pawn/D2/D3")
    response8 = app.test_client().delete("api/v1/Pawn/D2/D3")
    response9 = app.test_client().get("api/v1/KiNg/d1/E2")

    assert response.status_code == 200
    assert response.json["move"] == "valid"
    assert response.json["figure"] == "rook"
    assert response.json["error"] == "null"
    assert response.json["currentField"] == "H1"
    assert response.json["destField"] == "H2"

    assert response2.status_code == 409
    assert response2.json["move"] == "invalid"
    assert response2.json["figure"] == "rook"
    assert response2.json["error"] == "Current move is not permitted"
    assert response2.json["currentField"] == "H1"
    assert response2.json["destField"] == "B2"

    assert response3.status_code == 500

    assert response4.status_code == 409
    assert response4.json["move"] == "invalid"
    assert response4.json["figure"] == "knight"
    assert response4.json["error"] == "Field does not exist"
    assert response4.json["currentField"] == "A1"
    assert response4.json["destField"] == "E10"

    assert response5.status_code == 409
    assert response5.json["move"] == "invalid"
    assert response5.json["figure"] == "queen"
    assert response5.json["error"] == "You cannot move on the same place"
    assert response5.json["currentField"] == "D1"
    assert response5.json["destField"] == "D1"

    assert response6.status_code == 405
    assert response7.status_code == 405
    assert response8.status_code == 405

    assert response9.status_code == 200
    assert response9.json["move"] == "valid"
    assert response9.json["figure"] == "king"
    assert response9.json["error"] == "null"
    assert response9.json["currentField"] == "D1"
    assert response9.json["destField"] == "E2"
