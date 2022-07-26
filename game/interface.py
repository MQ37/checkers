from .color import Color


class CLIInterface:

    def __init__(self):
        self.nicknames = {}

    def interface_surrender(self, game, player_loser, player_winner):
        certainty = input(
            "Are you really sure you want to surrender? Type Y/N ⇉ ")
        if certainty == "Y":
            print(f"{player_loser} gave up. Winner is {player_winner}!")
            game.export_csv('save.csv')
            quit()
        elif certainty == "N":
            return (None)

        while not certainty == ("Y" or "N"):
            certainty = input("Oh common! Just type Y/N ⇉ ")
            if certainty == "Y":
                print(f"{player_loser} gave up. Winner is {player_winner}!")
                game.export_csv('save.csv')
                quit()
            elif certainty == "N":
                return (None)

    def _get_player_nick(self, player):
        return self.nicknames.get(player.color, repr(player))

    def menu(self, game):
        options = (
            (1, "Start new game for two players"),
            (2, "Start new game with AI"),
            (3, "Load game from CSV for two players"),
            (4, "Load game from CSV with AI"),
        )

        for opt in options:
            print("%s: %s" % opt)

        choice = int(input("Choice: "))
        while not choice in range(1, len(options) + 1):
            choice = int(input("Wrong choice: "))

        if choice == 1:
            return {"load": None, "ai": False}
        elif choice == 2:
            return {"load": None, "ai": True}
        elif choice in range(3, 4 + 1):
            path = input("Path to CSV file: ")
            if choice == 3:
                return {"load": path, "ai": False}
            elif choice == 4:
                return {"load": path, "ai": True}

    def interface_turn(self, board, player, playable_figures):
        board.pretty_print()

        player_nickname = self._get_player_nick(player)
        out_header = f"----{player_nickname} is picking his next move----"
        print(out_header)

        for i, fig in enumerate(playable_figures):
            print("%s: %s" %
                  (i + 1, playable_figures[fig].root.value.notation))

        choice = int(input("\nChoose your figure from above! ⇉ "))
        while not choice in range(1, len(playable_figures) + 1):
            choice = int(
                input("There is no such figure, try different choice! ⇉ "))

        figure = list(playable_figures.keys())[choice - 1]
        tree = playable_figures[figure]
        moves, taking_moves = tree.as_moves(split_taking=True)

        if taking_moves:
            valid_moves = taking_moves
        else:
            valid_moves = moves

        for i, path in enumerate(valid_moves):
            print("%s: %s" %
                  (i + 1, " -> ".join(map(lambda pos: pos[0].notation, path))))

        # Print footer
        for _ in range(len(out_header)):
            print("-", end="")

        choice = int(input("\nChoose your next move from above! ⇉ "))
        while not choice in range(1, len(valid_moves) + 1):
            choice = int(input("There is no such move, try different one! ⇉ "))

        return (valid_moves[choice - 1])

    def ask_nicknames(self, ai=False):
        nick_w = input("Choose white player nickname: ")
        self.nicknames[Color.WHITE] = nick_w
        if not ai:
            nick_b = input("Choose black player nickname: ")
            self.nicknames[Color.BLACK] = nick_b

    def show_winner(self, player):
        player_nickname = self._get_player_nick(player)
        print("----- Winner is %s -----" % player_nickname)
