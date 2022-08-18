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

    # Gets best move by number of takes
    def _best_move(self, playable_figures):
        best_count = 0
        best_move = None
        for figure in playable_figures:
            tree = playable_figures[figure]
            moves, taking_moves = tree.as_moves(split_taking=True)
            for move in taking_moves:
                count = 0
                for node in move:
                    # If is taking
                    if node[1]:
                        count += 1
                if count > best_count:
                    best_count = count
                    best_move = move

        return best_move

    def play_turn(self, board, interface):
        # Get playable figures
        playable_figures = board.get_player_playable_figures(self)
        if not playable_figures:
            return None

        # Get random move
        move = self._best_move(playable_figures)
        if not move:
            move = self._random_move(playable_figures)

        interface.show_move(self, move)

        # Execute the moves
        pos_from = move[0][0]
        for m in move[1:]:
            pos_to = m[0]
            pos_taking = m[1]
            board.move(self, pos_from, pos_to, pos_taking)
            pos_from = pos_to

        return move

    def __repr__(self):
        return "AI (%s)" % self.color
