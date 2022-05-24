def interface_surrender(player_loser, player_winner): # maybe player1, player2 ?
    certainty = input("Are you really sure you want to surrender? Type Y/N ⇉ ")
    if certainty == "Y":
            print(f"{player_loser} gave up. Winner is {player_winner}!") # TODO have to add NEXT PLAYER wins
            quit()

    while not certainty == ("Y" or "N"):
        certainty = input("Oh common! Just type Y/N ⇉ ")
        if certainty == "Y":
            print(f"{player_loser} gave up. Winner is {player_winner}!") #TODO winner is the second player
            quit()
            
def interface_move(player_nickname, moves):
    out_header = f"----{player_nickname} is picking his next move----"
    print(out_header)

    for move in range(len(moves)):
        print(f"{move+1}: {moves[move]}")

    [print("-", end = "") for i in range(len(out_header))]   # flexible ("footer") according to length of "header"

    choice = int(input("\nChoose your next move from above! ⇉ "))
    while not choice in range (1, len(moves)+1):
        choice = int(input("There is no such move, try different one! ⇉ "))
    
    return(moves[choice-1])
