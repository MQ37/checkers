import random
from .player import Player


class AI(Player):

    def _random_move(self, playable_figures):
        figure = random.choice(list(playable_figures.keys()))
        tree = playable_figures[figure]
        moves, taking_moves = tree.as_moves(split_taking=True)

        if taking_moves:
            valid_moves = taking_moves
        else:
            valid_moves = moves

        return random.choice(valid_moves)

    def play_turn(self, board, interface):
        # Get playable figures
        playable_figures = board.get_player_playable_figures(self)

        # Get random move
        move = self._random_move(playable_figures)

        interface.show_move(self, move)

        # Execute the moves
        pos_from = move[0][0]
        for m in move[1:]:
            pos_to = m[0]
            pos_taking = m[1]
            board.move(self, pos_from, pos_to, pos_taking)
            pos_from = pos_to

    def __repr__(self):
        return "AI (%s)" % self.color
