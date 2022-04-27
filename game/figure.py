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

    def set_field(self, field):
        self.field = field

    def remove_field(self):
        field = self.field
        self.field = None
        return field
