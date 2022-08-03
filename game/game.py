from .board import Board
from .player import Player
from .color import Color
from .ai import AI


class Game:

    def __init__(self, interface):
        self.board = Board()
        self.interface = interface

        settings = interface.menu(self)

        self.player_w = Player(Color.WHITE)
        if settings["ai"]:
            self.player_b = AI(Color.BLACK)
            interface.ask_nicknames(ai=True)
        else:
            self.player_b = Player(Color.BLACK)
            interface.ask_nicknames()
        self.nturns = 0

        if settings["load"]:
            self.load_csv(settings["load"])
        else:
            self.board.populate_board(self.player_w, self.player_b)

    def export_csv(self, path):
        try:
            with open(path, "w",
                      newline='') as f:  # newline for avoiding blank lines
                f.write(self.board.export())
                print("Game was saved.")
        except Exception:
            print("WRONG DATA FORMAT - Check the data. ---> export_csv")

    def load_csv(self, path):
        self.board.load(self.player_w, self.player_b, path)

    def _get_current_player(self):
        if self.nturns % 2 == 0:
            return self.player_w
        else:
            return self.player_b

    def turn(self):
        player = self._get_current_player()

        move = player.play_turn(self.board, self.interface)

        # Log move
        self.board.log_move(move)

        # If winner show and exit
        winner = self.board.check_win()
        if winner:
            self.interface.show_winner(winner)
            exit()

        self.board.transform_mans_to_kings(self.player_w, self.player_b)

        self.nturns += 1
