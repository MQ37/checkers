import math
import string

from .field import Field
from .color import Color
from .coord_map import COORD_MAP_R, COORD_MAP_L
from re import match, findall

from .figure import Figure
from .king import King
from .player import Player


class Board:
    CORRECT_NOTATION = r'^([A-H])([1-8])$'
    BOARD_SIZE = 8

    # when size = 8
    # [0][0] is A1
    # [0][1] is B1
    # [7][6] is F8
    # [7][7] is H8
    # board[0] is first row "1"
    # board[1] is second row "2"
    # board[7] is eight row "7"

    def __init__(self):
        self._board = self._generate_board()
        self._positions = {}

    # coords -> (str, int) | ("A", 1) or str | "A1"
    def field_at(self, notation: string):
        assert match(Board.CORRECT_NOTATION, notation), f'Incorrect notation coords ({notation})'
        j, i = findall(Board.CORRECT_NOTATION, notation)[0]
        # So coords can also be string "A1" or tuple ("A", 1)
        return self.field_at_indexes((COORD_MAP_L[j] - 1, int(i) - 1))

    # index -> (int, int) | (0, 0)
    def field_at_indexes(self, idxs) -> Field:
        assert 0 <= idxs[0] < 8, f'Bad coordinates {idxs}'
        assert 0 <= idxs[1] < 8, f'Bad coordinates {idxs}'

        return self._board[idxs[0]][idxs[1]]

    def pretty_print(self):
        for row in reversed(self._board):
            heading = "|"
            content = "|"

            for field in row:
                x, y = field.coords
                if field.color == Color.BLACK:
                    col_heading = "▮ %s%s ▮" % (x, y)
                else:
                    col_heading = "▯ %s%s ▯" % (x, y)

                if field.figure:
                    if field.figure.color == Color.BLACK:
                        col_content = "▮"
                    else:
                        col_content = "▯"
                else:
                    col_content = ""

                len_col_heading = len(col_heading)
                len_col_content = len(col_content)
                if len_col_heading > len_col_content:
                    delta = len_col_heading - len_col_content
                    col_content = (" " * math.floor(delta / 2)) + col_content
                    col_content += " " * math.ceil(delta / 2)
                else:
                    delta = len_col_content - len_col_heading
                    col_heading = (" " * math.floor(delta / 2)) + col_heading
                    col_heading += " " * math.ceil(delta / 2)

                col_heading = " %s |" % col_heading
                col_content = " %s |" % col_content

                heading += col_heading
                content += col_content

            length = len(heading)
            print("-" * length)
            print(heading)
            print(content)
        print("-" * length)

    # c_from is coords to move figure from
    # c_to is coords to move figure to
    def move_figure(self, player: Player, c_from: tuple[int], c_to: tuple[int]):
        f_from = self.field_at_indexes(c_from)
        f_to = self.field_at_indexes(c_to)

        # From field is empty and Target field is full and figure is of moving player
        if not f_from.figure and f_to.figure and f_from.figure.owner == player:
            return False

        moving_figure = f_from.figure
        f_from.clear()
        f_to.figure = moving_figure

    # Exports boards state to CSV format
    # returns CSV string
    def export(self):
        lines = ""
        for row in self._board:
            for field in row:
                if field.figure:
                    pos = field.coords
                    line = "%s%s," % pos
                    if field.figure.color == Color.WHITE:
                        if type(field.figure) == King:
                            line += "ww"
                        else:
                            line += "w"
                    else:
                        if type(field.figure) == King:
                            line += "bb"
                        else:
                            line += "b"
                    lines += "%s\n" % line
        return lines

    def populate_board(self, player_w, player_b):
        pos_w = ["A1", "A3", "B2", "C1", "C3", "D2",
                 "E1", "E3", "F2", "G1", "G3", "H2"]
        pos_b = ["A7", "B6", "B8", "C7", "D6", "D8",
                 "E7", "F6", "F8", "G7", "H6", "H8"]

        for pos in pos_w:
            figure = player_w.create_figure()
            self.field_at(pos).figure = figure
            self._add_position(figure, pos)

        for pos in pos_b:
            figure = player_b.create_figure()
            self.field_at(pos).figure = figure
            self._add_position(figure, pos)

    @staticmethod
    def _generate_board() -> list[list[Field]]:
        board = []

        for i in range(Board.BOARD_SIZE):
            row = []

            for j in range(Board.BOARD_SIZE):
                color = Color.BLACK if (j + i) % 2 == 0 else Color.WHITE

                # (j, i) coords are swapped
                row.append(Field(color, coords=(j, i)))

            board.append(row)

        return board

    def _add_position(self, figure, pos):
        idx_pos = (COORD_MAP_L[pos[0]]-1, int(pos[1])-1)

        self._positions[figure] = idx_pos

    def location(self, figure: Figure):
        return self._positions.get(figure)
