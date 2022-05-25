import game
from game.position import Position
from game.interface import CLIInterface

interface = CLIInterface()
interface.ask_nicknames()

game = game.Game(interface)

while True:
    game.turn()

#def npo(pos):
#    return Position.from_notation(pos)
#
#pb = game.player_b
#pw = game.player_w
#
#game.board._move_figure(pb, npo("B6"), npo("C5"))
#game.board._move_figure(pb, npo("D6"), npo("E5"))
#game.board._move_figure(pw, npo("A3"), npo("B4"))
#
#game.board.pretty_print()
#
#figure = game.board.field_at(npo("B4")).figure
#print(figure)
#print(game.board.location(figure))
#possible_moves = figure.possible_moves(game.board)
#for move in possible_moves.root.children:
#    print(repr(move))
#    print("---")

#fpos = Position.from_notation("D6")
#npos = Position.from_notation("D4")
#ofield = game.board.field_at(fpos)
#figure = ofield.figure
#ofield.clear()
#nfield = game.board.field_at(npos)
#nfield.figure = figure
#figure.field = nfield
#
#pos = Position.from_notation("G7")
#field = game.board.field_at(pos)
#field.clear()
#
#game.board.pretty_print()
#
#pos = Position.from_notation("C3")
#possible_moves = game.board.field_at(pos).figure.possible_moves(game.board)
#print(pos.notation, pos.tuple)
#print()
#for move in possible_moves.root.children:
#    print(repr(move))
#    print("---")
#
#print(game.board._positions)
#
#print()

