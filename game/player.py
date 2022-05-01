from .man import Man
from .king import King

class Player():

    figures = None
    color = None
    board = None

    def __init__(self, color, board):
        self.figures = []
        self.color = color
        self.board = board

    # Getters and setters
    def get_figures(self):
        return self.figures

    def get_color(self):
        return self.color

    def create_figure(self, king=False):
        figure = Man(self)
        self.figures.append(figure)
        return figure
