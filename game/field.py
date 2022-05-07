from typing import Optional

from .color import Color
from .figure import Figure
from .helpers import coords_to_index
from .coord_map import COORD_MAP_R, COORD_MAP_L


class Field:
    def __init__(self, color: Color, coords: tuple[int, int], figure: Optional[Figure] = None):
        # White, Black
        self._color = color
        # (X, Y)
        self._coords = coords
        # Contained figure
        self._figure = figure

    # Getters and setters
    @property
    def figure(self) -> Optional[Figure]:
        return self._figure

    @figure.setter
    def figure(self, figure: Figure):
        self._figure = figure

    @property
    def color(self):
        return self._color

    @property
    def coords(self):
        return self._coords

    @property
    def coords_notation(self):
        return f'{COORD_MAP_R[self._coords[1] + 1]}{8 - self._coords[0]}'

    @property
    def position(self) -> tuple[int, int]:
        return self._coords

    def clear(self):
        self._figure = None

    # Str Repr
    def __str__(self):
        if self.figure:
            return "Field (%s) at %s containing %s" % (self.color, self.coords, self.figure)
        else:
            return "Field (%s) at %s containing Nothing" % (self.color, self.coords)

    def __repr__(self):
        return str(self)
