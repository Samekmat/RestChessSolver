from flask import Flask, jsonify
from abc import ABC, abstractmethod

app = Flask(__name__)


@app.route("/", methods=["GET"])
def test():
    return jsonify({0: "test"})


class Figure(ABC):
    def __init__(self, position):
        self.currentField = position
        
    @abstractmethod
    def list_available_moves(self):
        self.all_moves = [
            ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1'],
            ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'],
            ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'],
            ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'],
            ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'],
            ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'],
            ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'],
            ['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8'],
        ]

    def find_current_index(self):
        for sub_list in self.all_moves:
            if self.currentField in sub_list:
                self.current_index = (self.all_moves.index(sub_list), sub_list.index(self.currentField))
                return self.current_index

    def validate_move(self, dest_field):
        return 'valid' if dest_field in self.availableMoves else 'invalid'


class Pawn(Figure):
    def list_available_moves(self):
        super().list_available_moves()
        super().find_current_index()
        self.availableMoves = []
        i = self.current_index
        self.availableMoves.append(self.all_moves[i[0] + 1][i[1]])

        return self.availableMoves


class Knight(Figure):
    def list_available_moves(self):
        super().list_available_moves()
        super().find_current_index()
        i = self.current_index
        self.availableMoves = []

        for lin, l in enumerate(self.all_moves):
            # lin = index of a nested list in all_moves list
            for index, value in enumerate(l):
                if abs((i[0] - lin) * (i[1] - index)) == 2:
                    self.availableMoves.append(self.all_moves[lin][index])
        
        return sorted(self.availableMoves)


class Bishop(Figure):
    def list_available_moves(self):
        super().list_available_moves()
        super().find_current_index()
        i = self.current_index
        self.availableMoves = []

        for lin, l in enumerate(self.all_moves):
            # lin = index of a nested list in all_moves list
            for index, value in enumerate(l):
                if abs(lin - i[0]) == abs(index - i[1]) > 0:
                    self.availableMoves.append(self.all_moves[lin][index])

        return sorted(self.availableMoves)


class Rook(Figure):
    def list_available_moves(self):
        super().list_available_moves()
        super().find_current_index()
        self.availableMoves = []
        i = self.current_index

        for pos in range(8):
            if pos != i[0]:
                self.availableMoves.append(self.all_moves[pos][i[1]])
            if pos != i[1]:
                self.availableMoves.append(self.all_moves[i[0]][pos])

        return sorted(self.availableMoves)


class Queen(Figure):
    def list_available_moves(self):
        super().list_available_moves()
        super().find_current_index()
        pass


class King(Figure):
    def list_available_moves(self):
        super().list_available_moves()
        super().find_current_index()
        i = self.current_index
        self.availableMoves = []

        for x in range(8):
            for y in range(8):
                if(max(abs(x - i[0]), abs(y - i[1])) ==1):
                    self.availableMoves.append(self.all_moves[x][y])
        return sorted(self.availableMoves)


if __name__ == "__main__":
    app.run(debug=True)
