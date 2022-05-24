# TODO check surrender
# return 0 if player changed his mind

def interface_surrender(player): # maybe player1, player2 ?
    certainty = input("Are you really sure you want to surrender? Type Y/N ⇉ ")
    if certainty == "Y":
            print(f"Winner is {player}.") # TODO have to add NEXT PLAYER wins
            quit()
    elif certainty == "N":
        return(0)

    while not certainty == ("Y" or "N"):
        certainty = input("Oh common! Just type Y/N ⇉ ")
        if certainty == "Y":
            print(f"Winner is ⇉ {player}.") #TODO winner is the second player
            quit()
        elif certainty == "N":
            return(0)

# TODO check move

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
