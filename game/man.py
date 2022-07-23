from .figure import Figure
from .color import Color
from .position import Position
from .tree.tree import Tree
from .tree.tree_node import TreeNode


class Man(Figure):

    def possible_moves(self, board) -> Tree:
        cur_pos: Position = board.location(self)

        moves = []

        allow_up = self.color == Color.WHITE
        allow_down = self.color == Color.BLACK

        for pos in board.locations_around(cur_pos,
                                          allow_up=allow_up,
                                          allow_down=allow_down):
            if board.is_field_empty(pos):
                moves.append(TreeNode(pos))
            elif board.field_at(pos).figure.owner != self.owner:
                width_diff, height_diff = pos.diff(cur_pos)

                take_position = pos.move(width_diff, height_diff)

                if take_position and board.is_field_empty(take_position):
                    moves.append(
                        TreeNode(take_position,
                                 taking=pos,
                                 children=self._possible_takes(
                                     board, take_position, allow_up,
                                     allow_down)))

        return Tree(TreeNode(cur_pos, children=tuple(moves)))

    def _possible_takes(self, board, cur_pos: Position, allow_up, allow_down):
        moves = []

        for pos in board.locations_around(cur_pos,
                                          allow_up=allow_up,
                                          allow_down=allow_down):
            if not board.is_field_empty(
                    pos) and board.field_at(pos).figure.owner != self.owner:
                width_diff, height_diff = pos.diff(cur_pos)

                take_position = pos.move(width_diff, height_diff)

                if take_position and board.is_field_empty(take_position):
                    moves.append(
                        TreeNode(
                            take_position,
                            self._possible_takes(board, take_position,
                                                 allow_up, allow_down)))

        return tuple(moves)

    def __repr__(self):
        return f'Man(color: {self.color}, owner: {self.owner})'
