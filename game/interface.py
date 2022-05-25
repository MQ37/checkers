from .color import Color

class CLIInterface:

    def __init__(self):
        self.nicknames = {}

    def interface_surrender(self, game, player_loser, player_winner):
        certainty = input("Are you really sure you want to surrender? Type Y/N ⇉ ")
        if certainty == "Y":
            print(f"{player_loser} gave up. Winner is {player_winner}!")
            game.export_csv('save.csv')
            quit()
        elif certainty == "N":
            return(None)

        while not certainty == ("Y" or "N"):
            certainty = input("Oh common! Just type Y/N ⇉ ")
            if certainty == "Y":
                print(f"{player_loser} gave up. Winner is {player_winner}!")
                game.export_csv('save.csv')
                quit()
            elif certainty == "N":
                return(None)

    def _get_player_nick(self, player):
        return self.nicknames.get(player.color, repr(player))

    def interface_turn(self, board,player, playable_figures):
        board.pretty_print()

        player_nickname = self._get_player_nick(player)
        out_header = f"----{player_nickname} is picking his next move----"
        print(out_header)

        for i, fig in enumerate(playable_figures):
            print("%s: %s" % (i+1, playable_figures[fig].root.value.notation))

        choice = int(input("\nChoose your figure from above! ⇉ "))
        while not choice in range (1, len(playable_figures)+1):
            choice = int(input("There is no such figure, try different choice! ⇉ "))

        figure = list(playable_figures.keys())[choice-1]
        tree = playable_figures[figure]
        moves = tree.as_moves()

        #for move in range(len(moves)):
        #    print(f"{move+1}: {moves[move]}")
        for i, path in enumerate(moves):
            print(path)
            print("%s: %s" % (i+1, " -> ".join( map(lambda pos: pos[0].notation, path) ) ) )

        [print("-", end = "") for i in range(len(out_header))]   # flexible ("footer") according to length of "header"

        choice = int(input("\nChoose your next move from above! ⇉ "))
        while not choice in range (1, len(moves)+1):
            choice = int(input("There is no such move, try different one! ⇉ "))
        
        return(moves[choice-1])

    def ask_nicknames(self):
        nick_w = input("Choose white player nickname: ")
        nick_b = input("Choose black player nickname: ")
        self.nicknames[Color.WHITE] = nick_w
        self.nicknames[Color.BLACK] = nick_b
