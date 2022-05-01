import math

from .field import Field
from .color import Color
from .coord_map import COORD_MAP_R, COORD_MAP_L
from .man import Man
from .king import King

class Board():

    # when size = 8
    # [0][0] is A1
    # [0][1] is B1
    # [7][6] is F8
    # [7][7] is H8
    # board[0] is first row "1"
    # board[1] is second row "2"
    # board[7] is eight row "7"
    board = None

    def __init__(self, size):
        self._generate_board(size)

    # Getters
    def get_size(self):
        return len(self.board)

    def get_board(self):
        return self.board

    # coords -> (str, int) | ("A", 1) or str | "A1"
    def get_field_at(self, coords):
        j, i = coords
        # So coords can also be string "A1" or tuple ("A", 1)
        i = int(i)
        j = COORD_MAP_L[j]
        return self.board[i-1][j-1]

    # index -> (int, int) | (0, 0)
    def get_field_at_index(self, index):
        j, i = index
        return self.board[i][j]

    def _generate_board(self, size):
        board = []
        for i in range(size):
            row = []
            for j in range(size):
                color = Color.BLACK if (j + i) % 2 == 0 else Color.WHITE
                # (j, i) coords are swapped
                coords = ( COORD_MAP_R[j+1], i+1 )
                field = Field(color, coords)
                row.append(field)
            board.append(row)
        self.board = board

    def pretty_print(self):
        for row in self.board:
            heading = "|"
            content = "|"
            for field in row:
                x, y = field.get_coords()
                if field.get_color() == Color.BLACK:
                    col_heading = "▮ %s%s ▮" % (x, y)
                else:
                    col_heading = "▯ %s%s ▯" % (x, y)

                if field.get_figure():
                    if field.get_figure().get_color() == Color.BLACK:
                        col_content = "▮"
                    else:
                        col_content = "▯"
                else:
                    col_content = ""


                len_col_heading = len(col_heading)
                len_col_content = len(col_content)
                if len_col_heading > len_col_content:
                    delta = len_col_heading - len_col_content
                    col_content = (" " * math.floor(delta/2)) + col_content
                    col_content += " " * math.ceil(delta/2)
                else:
                    delta = len_col_content - len_col_heading
                    col_heading = (" " * math.floor(delta/2)) + col_heading
                    col_heading += " " * math.ceil(delta/2)

                col_heading = " %s |" % col_heading
                col_content = " %s |" % col_content

                heading += col_heading
                content += col_content

            length = len(heading)
            print( "-"*length )
            print(heading)
            print(content)
        print( "-"*length )

    # cfrom is coords to move figure from
    # cto is coords to move figure to
    def move_figure(self, cfrom, cto):
        ffrom = self.get_field_at(cfrom)
        fto = self.get_field_at(cto)

        # From field is empty
        if not ffrom.get_figure():
            return False
        # Target field is full
        if fto.get_figure():
            return False

        figure = ffrom.remove_figure()
        fto.set_figure(figure)
        figure.set_field(fto)

    # Exports boards state to CSV format
    # returns CSV string
    def export(self):
        lines = ""
        for row in self.board:
            for field in row:
                if field.get_figure():
                    pos = field.get_coords()
                    line = "%s%s," % pos
                    if field.get_figure().get_color() == Color.WHITE:
                        if type(field.get_figure()) == King:
                            line += "ww"
                        else:
                            line += "w"
                    else:
                        if type(field.get_figure()) == King:
                            line += "bb"
                        else:
                            line += "b"
                    lines += "%s\n" % line
        return lines
