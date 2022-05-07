import math

from .field import Field
from .color import Color

from .king import King
from .player import Player
from .position import Position


class Board:
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
        self._board: list[list[Field]] = list(self._generate_board())
        self._positions = {}

    # coords -> (str, int) | ("A", 1) or str | "A1"
    def field_at(self, pos: Position) -> Field:
        # So coords can also be string "A1" or tuple ("A", 1)
        return self._board[pos.row][pos.col]

    def is_field_empty(self, pos: Position):
        return self.field_at(pos).figure is None

    @staticmethod
    def locations_around(pos: Position, allow_down=True, allow_up=True) -> list[Position]:
        locations_around = []

        if allow_up and pos.row - 1 >= 0 and pos.col - 1 >= 0:
            locations_around.append(pos.move(-1, -1))

        if allow_up and pos.row - 1 >= 0 and pos.col + 1 < Board.BOARD_SIZE:
            locations_around.append(pos.move(-1, +1))

        if allow_down and pos.row + 1 < Board.BOARD_SIZE and pos.col - 1 >= 0:
            locations_around.append(pos.move(+1, -1))

        if allow_down and pos.row + 1 < Board.BOARD_SIZE and pos.col + 1 < Board.BOARD_SIZE:
            locations_around.append(pos.move(+1, +1))

        return locations_around

    def pretty_print(self):
        for row in self._board:
            heading = "|"
            content = "|"

            for field in row:
                if field.color == Color.BLACK:
                    col_heading = "▮ %s ▮" % field.position.notation
                else:
                    col_heading = "▯ %s ▯" % field.position.notation

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
    def move_figure(self, player: Player, pos_from: Position, pos_to: Position):
        field_from = self.field_at(pos_from)
        field_to = self.field_at(pos_to)

        # From field is empty and Target field is full and figure is of moving player
        if not field_from.figure and field_to.figure and field_from.figure.owner == player:
            return False

        moving_figure = field_from.figure
        field_from.clear()
        field_to.figure = moving_figure

        return True

    # Exports boards state to CSV format
    # returns CSV string
    def export(self):
        lines = ""
        for row in self._board:
            for field in row:
                if field.figure:
                    pos = field.position.notation
                    line = "%s," % pos
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

        for pos in map(Position.from_notation, pos_w):
            figure = player_w.create_figure()
            self.field_at(pos).figure = figure
            self._add_position(figure, pos)

        for pos in map(Position.from_notation, pos_b):
            figure = player_b.create_figure()
            self.field_at(pos).figure = figure
            self._add_position(figure, pos)


    def populate_board2(self, player_w, player_b):
        pos_w = ["A1", "A3", "C3", "D2", "D4", "E1", "F2", "G1"]
        pos_b = ["B8", "C7", "C5", "D6", "H8"]

        for pos in map(Position.from_notation, pos_w):
            figure = player_w.create_figure()
            self.field_at(pos).figure = figure
            self._add_position(figure, pos)

        for pos in map(Position.from_notation, pos_b):
            figure = player_b.create_figure()
            self.field_at(pos).figure = figure
            self._add_position(figure, pos)


    @staticmethod
    def _color_match(row, col):
        return Color.BLACK if (row + col) % 2 == 0 else Color.WHITE

    @staticmethod
    def _generate_board() -> list[list[Field]]:
        for row in range(Board.BOARD_SIZE):
            yield [
                Field(Board._color_match(row, col), Position(row, col)) for col in range(Board.BOARD_SIZE)
            ]

    def _add_position(self, figure, pos: Position):
        self._positions[figure] = pos

    def location(self, figure):
        return self._positions.get(figure)
