from .board import Board
from .player import Player
from .color import Color


class Game:
    def __init__(self):
        self.board = Board()
        self.player_w = Player(Color.WHITE)
        self.player_b = Player(Color.BLACK)

        self.board.populate_board(self.player_w, self.player_b)

    # TODO export to CSV file
    def export_csv(self):
        pass

    # TODO load from CSV file
    def load_csv(self):
        pass
