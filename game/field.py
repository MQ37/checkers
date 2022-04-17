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

    # Getters
    def get_figure(self):
        return self.figure

    def get_color(self):
        return self.color

    def get_coords(self):
        return self.coords

    # Str Repr
    def __str__(self):
        return "Field (%s) at %s containing %s" % (self.color, self.coords,
                                                    self.figure)

    def __repr__(self):
        return str(self)

