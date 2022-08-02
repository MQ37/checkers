from abc import ABC

from game.color import Color
from game.tree.tree import Tree


class Figure(ABC):

    def __init__(self, owner):
        self._owner = owner

    @property
    def color(self) -> Color:
        return self._owner.color

    @property
    def owner(self):
        return self._owner

    def possible_moves(self, board) -> Tree:
        raise NotImplemented('Abstract method')

    def remove_figure(self):
        self._owner.remove_figure(self)
