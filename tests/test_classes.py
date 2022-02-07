from resources.chess import Figure, Pawn, Knight, Bishop, Rook, Queen, King


def test_pawn_class():
    p = Pawn("H1")
    p.list_available_moves()

    assert isinstance(p, Figure)
    assert p.currentField == "H1"
    assert p.availableMoves == ["H2"]
    assert p.validate_move("H2") == "valid"
    assert p.validate_move("H3") == "invalid"
    assert p.currentField not in p.availableMoves


def test_knight_class():
    k = Knight("C1")
    k.list_available_moves()

    assert isinstance(k, Figure)
    assert k.currentField == "C1"
    assert k.availableMoves == ["A2", "E2", "B3", "D3"]
    for i in k.availableMoves:
        assert k.validate_move(i) == "valid"
    assert k.validate_move("H8") != "valid"
    assert k.currentField not in k.availableMoves


def test_bishop_class():
    b = Bishop("E4")
    b.list_available_moves()

    assert isinstance(b, Figure)
    assert b.currentField == "E4"
    assert b.availableMoves == [
        "B1",
        "H1",
        "C2",
        "G2",
        "D3",
        "F3",
        "D5",
        "F5",
        "C6",
        "G6",
        "B7",
        "H7",
        "A8",
    ]
    for i in b.availableMoves:
        assert b.validate_move(i) == "valid"
    assert b.validate_move("C1") != "valid"
    assert b.currentField not in b.availableMoves


def test_rook_class():
    r = Rook("A1")
    r.list_available_moves()

    assert isinstance(r, Figure)
    assert r.currentField == "A1"
    for i in r.availableMoves:
        assert isinstance(i, str)

    for i in r.availableMoves:
        assert r.validate_move(i) == "valid"
    assert r.validate_move("D8") != "valid"
    assert r.currentField not in r.availableMoves


def test_queen_class():
    q = Queen("H1")
    q.list_available_moves()

    assert isinstance(q, Figure)
    assert q.currentField == "H1"
    for i in q.availableMoves:
        assert q.validate_move(i) == "valid"
    assert q.validate_move("G7") != "valid"
    assert q.currentField not in q.availableMoves


def test_king_class():
    k = King("E1")
    k.list_available_moves()
    k2 = King("e2")

    assert isinstance(k, Figure)
    assert isinstance(k2, Figure)
    assert k.currentField == "E1"
    for i in k.availableMoves:
        assert k.validate_move(i) == "valid"
    assert k.validate_move("A1") != "valid"
    assert k.currentField not in k.availableMoves
