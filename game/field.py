from typing import Optional

from .color import Color
from .helpers import coords_to_index
from .coord_map import COORD_MAP_R, COORD_MAP_L
from .position import Position


class Field:
    def __init__(self, color: Color, pos: Position, figure: Optional = None):
        # White, Black
        self._color = color
        # Position(row, col)
        self._pos = pos
        # Contained figure
        self._figure = figure

    # Getters and setters
    @property
    def figure(self) -> Optional:
        return self._figure

    @figure.setter
    def figure(self, figure):
        self._figure = figure

    @property
    def color(self):
        return self._color

    @property
    def position(self):
        return self._pos

    def clear(self):
        self._figure = None

    # Str Repr
    def __str__(self):
        if self.figure:
            return "Field (%s) at %s containing %s" % (self.color, self.position.notation, self.figure)
        else:
            return "Field (%s) at %s containing Nothing" % (self.color, self.position.notation)

    def __repr__(self):
        return str(self)
