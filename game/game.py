from pickle import TRUE
from .board import Board
from .player import Player
from .color import Color


class Game:
    def __init__(self):
        self.board = Board()
        self.player_w = Player(Color.WHITE, Player.nickname)
        self.player_b = Player(Color.BLACK, Player.nickname)

        self.board.populate_board(self.player_w, self.player_b)

    def export_csv(self, output):
        try:
            with open(output, "w", newline='') as file:  # newline for avoiding blank lines
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
                    if (inx[0] in valid_characters) and (inx[1] in valid_numbers) and (inx[2] == ',') and (inx[5:]) == '':
                        if ("w" or "ww") in inx[3:5]:  # inx[3:5] checks color
                            if "w" in inx[3] and inx[4] == '':
                                self.player_w.create_figure(inx)
                            else:
                                self.player_w.create_figure(inx, king=True)

                        elif ("b" or "bb") in inx[3:5]:  # inx[3:5] checks color
                            if "b" in inx[3] and inx[4] == '':
                                self.player_b.create_figure(inx)
                            else:
                                self.player_b.create_figure(inx, king=True)
                                
                        else:
                            raise Exception("WRONG DATA FORMAT - Check the data.")
                    else:
                        raise Exception("WRONG DATA FORMAT - Check the data.")
                return "Game was loaded."

        except:
            return "WRONG DATA FORMAT - Check the data."
