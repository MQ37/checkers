from .man import Man
from .king import King


class Player:
    def __init__(self, color):
        self._figures = []
        self._color = color

    # Getters and setters
    @property
    def figures(self):
        return self._figures

    @property
    def color(self):
        return self._color

    def create_figure(self, king=False):
        figure = King(self) if king else Man(self)
        self._figures.append(figure)
        return figure