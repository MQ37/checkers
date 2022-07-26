from .board import Board
from .player import Player
from .color import Color


class Game:

    def __init__(self, interface):
        self.board = Board()
        self.interface = interface

        settings = interface.menu(self)

        self.player_w = Player(Color.WHITE)
        if settings["ai"]:
            raise Exception("AI not implemented yet")
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

        # Get playable figures
        playable_figures = self.board.get_player_playable_figures(player)

        # Get selected move from the interface
        move = self.interface.interface_turn(self.board, player,
                                             playable_figures)

        # Execute the moves
        pos_from = move[0][0]
        for m in move[1:]:
            pos_to = m[0]
            pos_taking = m[1]
            self.board.move(player, pos_from, pos_to, pos_taking)
            pos_from = pos_to

        # If winner show and exit
        winner = self.board.check_win()
        if winner:
            self.interface.show_winner(winner)
            exit()

        self.nturns += 1
