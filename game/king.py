from .figure import Figure
from .position import Position
from .tree.tree import Tree
from .tree.tree_node import TreeNode


class King(Figure):
    def possible_moves(self, board):
        cur_pos: Position = board.location(self)

        moves = []

        for pos in board.locations_around(cur_pos, single=False):
            if board.is_field_empty(pos):
                moves.append(TreeNode(pos))
            elif board.field_at(pos).figure.owner != self.owner:
                width_diff, height_diff = pos.diff(cur_pos)

                take_position = None
                i = 1

                while True:
                    if take_position is None:
                        take_position = pos.move(width_diff*i, height_diff*i)

                        if take_position is None:
                            break

                    if not board.is_position_within_bounds(take_position):
                        break

                    if board.is_field_empty(take_position):
                        moves.append(TreeNode(take_position, taking=True, children=self._possible_takes(board, take_position)))

                    i += 1

        return Tree(TreeNode(cur_pos, tuple(moves)))

    def _possible_takes(self, board, cur_pos: Position):
        moves = []

        for pos in board.locations_around(cur_pos, single=True):
            if not board.is_field_empty(pos) and board.field_at(pos).figure.owner != self.owner:
                width_diff, height_diff = pos.diff(cur_pos)

                take_position = None
                i = 1

                while True:
                    if take_position is None:
                        take_position = pos.move(width_diff * i, height_diff * i)

                        if take_position is None:
                            break

                    if not board.is_position_within_bounds(take_position):
                        break

                    if board.is_field_empty(take_position):
                        moves.append(TreeNode(take_position, self._possible_takes(board, take_position)))

                    i += 1

        return tuple(moves)

    def __repr__(self):
        return f'King(color: {self.color}, owner: {self.owner})'
