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

    def remove_figure(self, figure):
        self._figures.remove(figure)

    def __repr__(self):
        return "Player (%s)" % self.color

    def __str__(self):
        return repr(self)

    def play_turn(self, board, interface):
        # Get playable figures
        playable_figures = board.get_player_playable_figures(self)
        if not playable_figures:
            return None

        # Get selected move from the interface
        move = interface.interface_turn(board, self, playable_figures)

        # Execute the moves
        pos_from = move[0][0]
        for m in move[1:]:
            pos_to = m[0]
            pos_taking = m[1]
            board.move(self, pos_from, pos_to, pos_taking)
            pos_from = pos_to

        return move
