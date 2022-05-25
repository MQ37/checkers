class Interface:
    # TODO fill __init__ ?
    def __init__(self):
        pass

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

    def interface_move(self, player_nickname, moves):
        out_header = f"----{player_nickname} is picking his next move----"
        print(out_header)

        for move in range(len(moves)):
            print(f"{move+1}: {moves[move]}")

        [print("-", end = "") for i in range(len(out_header))]   # flexible ("footer") according to length of "header"

        choice = int(input("\nChoose your next move from above! ⇉ "))
        while not choice in range (1, len(moves)+1):
            choice = int(input("There is no such move, try different one! ⇉ "))
        
        return(moves[choice-1])
