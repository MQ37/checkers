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
    def export_csv(self, output):
        try:
            with open(output, "w", newline='') as file:
                file.write(self.board.export())
                return "Game was saved."
        except:
            print("WRONG DATA FORMAT - Check the data. ---> export_csv")


    # TODO zeptat se na vstup (obecný) ?
    def load_csv(self, input):
        valid_characters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
        valid_numbers = ('1', '2', '3', '4', '5', '6', '7', '8')

        try:
            with open(input, "r") as file:
                file_reader = file.read()
                data = list(file_reader.split("\n"))

                for inx in data:
                    if (inx[0] in valid_characters) and (inx[1] in valid_numbers) and (inx[2] == ',') and (inx[5:]) == '':
                        if ("w" or"ww") in inx[3:5]:     # inx[3:5] checks color
                            self.playerw.create_figure(inx)
                        elif ("b" or "bb") in inx[3:5]:     # inx[3:5] checks color
                            self.playerb.create_figure(inx)
                        else:
                            raise Exception("WRONG DATA FORMAT - Check the data.")
                    else:
                        raise Exception("WRONG DATA FORMAT - Check the data.")
                return "Game was loaded."

        except:
            return "WRONG DATA FORMAT - Check the data."
