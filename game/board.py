import math
import re

from .field import Field
from .color import Color

from .king import King
from .player import Player
from .position import Position
from .helpers import BOARD_SIZE


class Board:

    def __init__(self):
        self._board: list[list[Field]] = list(self._generate_board())
        self._positions = {}

    def field_at(self, pos: Position) -> Field:
        return self._board[pos.row][pos.col]

    def is_field_empty(self, pos: Position):
        return self.field_at(pos).figure is None

    @staticmethod
    def locations_around(pos: Position,
                         allow_down=True,
                         allow_up=True,
                         single=True) -> list[Position]:
        locations_around = []

        for i in range(1, (1 if single else BOARD_SIZE) + 1):
            if allow_up and pos.row - i >= 0 and pos.col - i >= 0:
                locations_around.append(pos.move(-i, -i))

            if allow_up and pos.row - i >= 0 and pos.col + i < BOARD_SIZE:
                locations_around.append(pos.move(-i, +i))

            if allow_down and pos.row + i < BOARD_SIZE and pos.col - i >= 0:
                locations_around.append(pos.move(+i, -i))

            if allow_down and pos.row + i < BOARD_SIZE and pos.col + i < BOARD_SIZE:
                locations_around.append(pos.move(+i, +i))

        return locations_around

    @staticmethod
    def is_position_within_bounds(pos: Position):
        return 0 <= pos.row < BOARD_SIZE and 0 <= pos.col < BOARD_SIZE

    def pretty_print(self):
        for row in self._board:
            heading = "|"
            content = "|"

            for field in row:
                if field.color == Color.BLACK:
                    col_heading = "\u25A0 %s \u25A0" % field.position.notation
                else:
                    col_heading = "\u25A1 %s \u25A1" % field.position.notation

                if field.figure:
                    if field.figure.color == Color.BLACK:
                        if isinstance(field.figure, King):
                            col_content = "BB"
                        else:
                            col_content = "B"

                    else:
                        if isinstance(field.figure, King):
                            col_content = "WW"
                        else:
                            col_content = "W"
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
    def _move_figure(self, player: Player, pos_from: Position,
                     pos_to: Position):
        field_from = self.field_at(pos_from)
        field_to = self.field_at(pos_to)

        # From field is empty and Target field is full and figure is of moving player
        if not field_from.figure and field_to.figure and field_from.figure.owner == player:
            return False

        moving_figure = field_from.figure
        field_from.clear()
        field_to.figure = moving_figure

        self._positions[moving_figure] = pos_to

        return True

    def _remove_position(self, pos):
        field = self.field_at(pos)
        figure = field.figure

        # Remove from game state
        del self._positions[figure]
        field.clear()

        # Remove from owner
        figure.remove_figure()

    def _remove_figure(self, figure):
        pos = self.location(figure)
        self._remove_position(pos)

    def move(self, player, pos_from, pos_to, pos_taking=None):
        if pos_taking:
            field_taking = self.field_at(pos_taking)
            if field_taking.figure and field_taking.figure.owner is not player:
                self._remove_position(pos_taking)
        return self._move_figure(player, pos_from, pos_to)

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
                        if isinstance(field.figure, King):
                            line += "ww"
                        else:
                            line += "w"
                    else:
                        if isinstance(field.figure, King):
                            line += "bb"
                        else:
                            line += "b"
                    lines += "%s\n" % line
        return lines

    def load(self, player_w, player_b, path):
        with open(path, "r") as f:
            data = f.readlines()

            for i, line in enumerate(data):
                # Skip empty lines
                if not line.strip():
                    continue
                match = re.match("([A-H][1-8]),.*(ww|w|bb|b)$", line)
                if not match:
                    raise Exception("Invalid file format line %s: %s" %
                                    (i, line))

                pos_not, fig = match.groups()
                pos = Position.from_notation(pos_not)

                # White
                if fig.startswith("w"):
                    # TODO add support for King
                    figure = player_w.create_figure()
                    self.field_at(pos).figure = figure
                    self._add_position(figure, pos)
                # Black
                else:
                    # TODO add support for King
                    figure = player_b.create_figure()
                    self.field_at(pos).figure = figure
                    self._add_position(figure, pos)

    def populate_board(self, player_w, player_b):
        pos_w = [
            "A1", "A3", "B2", "C1", "C3", "D2", "E1", "E3", "F2", "G1", "G3",
            "H2"
        ]
        pos_b = [
            "A7", "B6", "B8", "C7", "D6", "D8", "E7", "F6", "F8", "G7", "H6",
            "H8"
        ]

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
        return Color.BLACK if (row + col) % 2 == 1 else Color.WHITE

    @staticmethod
    def _generate_board() -> list[list[Field]]:
        for row in range(BOARD_SIZE):
            yield [
                Field(Board._color_match(row, col), Position(row, col))
                for col in range(BOARD_SIZE)
            ]

    def _add_position(self, figure, pos: Position):
        self._positions[figure] = pos

    def location(self, figure):
        return self._positions.get(figure)

    # Returns figures as generator
    def get_player_figures(self, player):
        return filter(lambda fig: fig.owner is player, self._positions)

    # Returns dict figure -> tree
    def get_player_playable_figures(self, player):
        figures = self.get_player_figures(player)
        playable_figures = {}

        for fig in figures:
            tree = fig.possible_moves(self)
            # Skip figures without possible moves
            if not tree.root.children:
                continue
            playable_figures[fig] = tree

        # Figures that cat take have priority
        priority_figures = {}

        for fig in playable_figures:
            tree = playable_figures[fig]
            if any([child.taking for child in tree.root.children]):
                priority_figures[fig] = tree

        if priority_figures:
            return priority_figures

        return playable_figures

    # Returns None or player winner
    # TODO: check win in other scenarios
    # for example when figures are locked and no move is possible
    def check_win(self):
        potential_winner = list(self._positions.keys())[0].owner
        for figure in self._positions:
            if figure.owner is not potential_winner:
                return None
        return potential_winner
