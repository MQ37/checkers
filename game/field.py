from .helpers import coords_to_index

class Field():
    # Contained figure
    figure = None
    # White, Black
    color = None
    # (X, Y)
    coords = None

    def __init__(self, color, coords):
        self.color = color
        self.coords = coords

    # Getters and setters
    def get_figure(self):
        return self.figure

    def get_color(self):
        return self.color

    def get_coords(self):
        return self.coords

    def get_index(self):
        return coords_to_index(self.coords)

    def set_figure(self, figure):
        self.figure = figure

    def remove_figure(self):
        figure = self.figure
        self.figure = None
        return figure

    # Str Repr
    def __str__(self):
        return "Field (%s) at %s containing %s" % (self.color, self.coords,
                                                    self.figure)

    def __repr__(self):
        return str(self)

