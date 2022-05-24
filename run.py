import game
from game.coord_map import COORD_MAP_R
from game.helpers import index_to_coords
from game.position import Position

game = game.Game()


fpos = Position.from_notation("D6")
npos = Position.from_notation("D4")
ofield = game.board.field_at(fpos)
figure = ofield.figure
ofield.clear()
nfield = game.board.field_at(npos)
nfield.figure = figure
figure.field = nfield

pos = Position.from_notation("G7")
field = game.board.field_at(pos)
field.clear()

game.board.pretty_print()

pos = Position.from_notation("C3")
possible_moves = game.board.field_at(pos).figure.possible_moves(game.board)
print(pos.notation, pos.tuple)
print()
for move in possible_moves.root.children:
    print(repr(move))
    print("---")

print(game.board._positions)

print()

game.turn()