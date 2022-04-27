from .figure import Figure

class Player():

    figures = None
    color = None

    def __init__(self, color):
        self.figures = []
        self.color = color

    # Getters and setters
    def get_figures(self):
        return self.figures

    def get_color(self):
        return self.color

    def create_figure(self):
        figure = Figure(self)
        self.figures.append(figure)
        return figure
