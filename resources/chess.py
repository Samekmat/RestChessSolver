from abc import ABC, abstractmethod

BOARD = [
    ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"],
    ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],
    ["A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3"],
    ["A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4"],
    ["A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5"],
    ["A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6"],
    ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],
    ["A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8"],
]


class Figure(ABC):
    def __init__(self, position):
        self.currentField = position
        self.availableMoves = []

    @abstractmethod
    def list_available_moves(self):
        pass

    def find_current_index(self):
        for sub_list in BOARD:
            if self.currentField in sub_list:
                self.currentIndex = (
                    BOARD.index(sub_list),
                    sub_list.index(self.currentField),
                )
                return self.currentIndex

    def validate_move(self, dest_field):
        return "valid" if dest_field in self.availableMoves else "invalid"


class Pawn(Figure):
    def list_available_moves(self):
        super().list_available_moves()
        super().find_current_index()

        self.availableMoves.append(
            BOARD[self.currentIndex[0] + 1][self.currentIndex[1]]
        )

        return self.availableMoves


class Knight(Figure):
    def list_available_moves(self):
        super().list_available_moves()
        super().find_current_index()

        for x in range(8):
            for y in range(8):
                if abs((self.currentIndex[0] - x) * (self.currentIndex[1] - y)) == 2:
                    self.availableMoves.append(BOARD[x][y])

        return sorted(self.availableMoves)


class Bishop(Figure):
    def list_available_moves(self):
        super().list_available_moves()
        super().find_current_index()

        for x in range(8):
            for y in range(8):
                if abs(x - self.currentIndex[0]) == abs(y - self.currentIndex[1]) > 0:
                    self.availableMoves.append(BOARD[x][y])

        return sorted(self.availableMoves)


class Rook(Figure):
    def list_available_moves(self):
        super().list_available_moves()
        super().find_current_index()

        for x in range(8):
            if x != self.currentIndex[0]:
                self.availableMoves.append(BOARD[x][self.currentIndex[1]])
            if x != self.currentIndex[1]:
                self.availableMoves.append(BOARD[self.currentIndex[0]][x])

        return sorted(self.availableMoves)


class Queen(Figure):
    def list_available_moves(self):
        super().list_available_moves()
        super().find_current_index()

        for x in range(8):
            if x != self.currentIndex[0]:
                self.availableMoves.append(BOARD[x][self.currentIndex[1]])
            if x != self.currentIndex[1]:
                self.availableMoves.append(BOARD[self.currentIndex[0]][x])
            for y in range(8):
                if abs(x - self.currentIndex[0]) == abs(y - self.currentIndex[1]) > 0:
                    self.availableMoves.append(BOARD[x][y])

        return sorted(self.availableMoves)


class King(Figure):
    def list_available_moves(self):
        super().list_available_moves()
        super().find_current_index()

        for x in range(8):
            for y in range(8):
                if (
                    max(abs(x - self.currentIndex[0]), abs(y - self.currentIndex[1]))
                    == 1
                ):
                    self.availableMoves.append(BOARD[x][y])
        return sorted(self.availableMoves)


flatBoard = [item for sublist in BOARD for item in sublist]
