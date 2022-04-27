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
                print(coords)
                field = Field(color, coords)
                row.append(field)
            board.append(row)
        self.board = board
