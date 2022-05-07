from .coord_map import COORD_MAP_R, COORD_MAP_L
from re import match, findall


class Position:
    _CORRECT_NOTATION = r'^([A-H])([1-8])$'

    def __init__(self, row, col):
        assert 0 <= row < 8, f'Bad coordinates ({row}, {col})'
        assert 0 <= col < 8, f'Bad coordinates ({row}, {col})'

        self._row = row
        self._col = col

    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col

    @property
    def notation(self):
        return f'{COORD_MAP_R[self.col + 1]}{8-self.row}'

    @property
    def tuple(self):
        return self.row, self.col

    def move(self, width, height):
        return Position(self.row + width, self.col + height)

    def diff(self, pos):
        return self.row - pos.row, self.col - pos.col

    def __repr__(self):
        return f'Position(not: {self.notation}, pos: {(self.row, self.col)})'

    @staticmethod
    def from_notation(notation):
        assert match(Position._CORRECT_NOTATION, notation), f'Incorrect notation coords ({notation})'

        col, row = findall(Position._CORRECT_NOTATION, notation)[0]

        return Position(8 - int(row), COORD_MAP_L[col] - 1)

    def __eq__(self, other):
        if not isinstance(other, Position):
            return False

        return self.row == other.row and self.col == other.col
