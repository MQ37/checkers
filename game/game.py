from .board import Board
from .player import Player
from .color import Color

class Game():

    board = None
    playerw = None
    playerb = None

    def __init__(self):
        self.board = Board(8)
        self.playerw = Player(Color.WHITE, self.board)
        self.playerb = Player(Color.BLACK, self.board)

        self.board.populate_board(self.playerw, self.playerb)

    # TODO export to CSV file
    def export_csv(self):
        pass

    # TODO load from CSV file
    def load_csv(self):
        pass
