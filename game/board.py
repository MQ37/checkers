import math

from .field import Field
from .color import Color
from .coord_map import COORD_MAP_R, COORD_MAP_L

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
        return len(board)

    def get_board(self):
        return self.board

    def get_field_at(self, coords):
        j, i = coords
        # So coords can also be string "A1" or tuple ("A", 1)
        i = int(i)
        j = COORD_MAP_L[j]
        return self.board[i-1][j-1]

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
