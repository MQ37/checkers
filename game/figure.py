from abc import ABC

from game.color import Color
from game.tree.Tree import Tree


class Figure(ABC):
    def __init__(self, owner):
        self._owner = owner

    @property
    def color(self) -> Color:
        return self._owner.color

    @property
    def owner(self):
        return self._owner

    # TODO: represent moves as tree object
    # For figure there are none and all possible moves
    # they will be defined in child classes
    def possible_moves(self, board) -> Tree:
        raise NotImplemented('Abstract method')
