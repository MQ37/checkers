from .board import Board
from .player import Player
from .color import Color


class Game:

    def __init__(self, interface):
        self.board = Board()
        self.interface = interface
        self.player_w = Player(Color.WHITE)
        self.player_b = Player(Color.BLACK)
        self.nturns = 0

        self.board.populate_board(self.player_w, self.player_b)

    def export_csv(self, output):
        try:
            with open(output, "w",
                      newline='') as file:  # newline for avoiding blank lines
                file.write(self.board.export())
                return "Game was saved."
        except:
            print("WRONG DATA FORMAT - Check the data. ---> export_csv")

    def load_csv(self, input):
        valid_characters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
        valid_numbers = ('1', '2', '3', '4', '5', '6', '7', '8')

        try:
            with open(input, "r") as file:
                file_reader = file.read()
                data = list(file_reader.split("\n"))

                for inx in data:
                    if (inx[0] in valid_characters) and (
                            inx[1]
                            in valid_numbers) and (inx[2]
                                                   == ',') and (inx[5:]) == '':
                        if ("w" or "ww") in inx[3:5]:  # inx[3:5] checks color
                            self.player_w.create_figure(inx)
                        elif ("b"
                              or "bb") in inx[3:5]:  # inx[3:5] checks color
                            self.player_b.create_figure(inx)
                        else:
                            raise Exception(
                                "WRONG DATA FORMAT - Check the data.")
                    else:
                        raise Exception("WRONG DATA FORMAT - Check the data.")
                return "Game was loaded."

        except:
            return "WRONG DATA FORMAT - Check the data."

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
