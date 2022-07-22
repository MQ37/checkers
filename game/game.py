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
        else:
            self.player_b = Player(Color.BLACK)
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
                return "Game was saved."
        except:
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

        playable_figures = self.board.get_player_playable_figures(player)

        #for i, fig in enumerate(playable_figures):
        #    print("%s: %s" % (i, playable_figures[fig].root.value.notation))

        #sel = input("Select figure: ")
        #sel = int(sel)

        #figure = list(playable_figures.keys())[sel]
        #tree = playable_figures[figure]

        ## TODO: get moves by priority (taking)
        #moves = tree.as_moves()
        #for i, path in enumerate(moves):
        #    print(path)
        #    print("%s: %s" % (i, " -> ".join( map(lambda pos: pos[0].notation, path) ) ) )

        #sel = input("Select move: ")
        #sel = int(sel)
        move = self.interface.interface_turn(self.board, player,
                                             playable_figures)

        #move = moves[sel]
        pos_from = move[0][0]
        for m in move[1:]:
            print(m)
            pos_to = m[0]
            pos_taking = m[1]
            self.board.move(player, pos_from, pos_to, pos_taking)
            pos_from = pos_to

        self.nturns += 1
