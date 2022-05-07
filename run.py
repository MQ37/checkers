# run.py

import game
from game.coord_map import COORD_MAP_R
from game.helpers import index_to_coords
from game.position import Position
from game.tree.Tree import Tree

game = game.Game()

game.board.pretty_print()

pos = Position.from_notation("D4")
possible_moves = game.board.field_at(pos).figure.possible_moves(game.board)
print(pos.notation, pos.tuple)
print()
for move in possible_moves.root.children:
    print(repr(move))

print(game.board.export())
