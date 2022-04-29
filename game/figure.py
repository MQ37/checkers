class Figure():

    owner = None
    field = None

    def __init__(self, owner):
        self.owner = owner
        self.field = None

    # Getters and setters
    def get_owner(self):
        return self.owner

    def get_field(self):
        return self.field

    def get_color(self):
        return self.owner.get_color()

    def get_coords(self):
        return self.field.get_coords()

    def set_field(self, field):
        self.field = field

    def remove_field(self):
        field = self.field
        self.field = None
        return field

    # TODO: represent moves as tree object
    # For figure there are none and all possible moves
    # they will be defined in child classes
    def possible_moves(self, board):
        return None
