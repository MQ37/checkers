from .figure import Figure
from .position import Position
from .tree.tree import Tree
from .tree.tree_node import TreeNode
from .helpers import diff_to_allow, invert_single_allow, negate_allows


class King(Figure):

    # TODO: how to handle moves after taking, is taking after taking mandatory
    # or can we choose not to take after first take and move to field that has
    # no taking position? Right now taking after taking is not mandatory and
    # player can choose not to take after first take.
    # We need to check game rules
    def possible_moves(self, board):
        cur_pos: Position = board.location(self)

        moves = []

        for pos in board.locations_around(cur_pos, single=False):
            if board.is_field_empty(pos):
                moves.append(TreeNode(pos))
            elif board.field_at(pos).figure.owner != self.owner:
                width_diff, height_diff = pos.diff(cur_pos)

                allow_sw, allow_se, allow_nw, allow_ne = diff_to_allow(
                    width_diff, height_diff)

                for take_position in board.locations_around(pos,
                                                            single=False,
                                                            allow_down=False,
                                                            allow_up=False,
                                                            allow_sw=allow_sw,
                                                            allow_se=allow_se,
                                                            allow_nw=allow_nw,
                                                            allow_ne=allow_ne):
                    # If empty continue exploring
                    if board.is_field_empty(take_position):
                        moves.append(
                            TreeNode(
                                take_position,
                                taking=pos,
                                children=self._possible_takes(
                                    board,
                                    take_position,
                                    allows=negate_allows(*invert_single_allow(
                                        allow_sw, allow_se, allow_nw,
                                        allow_ne)))))
                    # If blocked by friendly figure stop
                    elif board.field_at(
                            take_position).figure.owner is self.owner:
                        break

        return Tree(TreeNode(cur_pos, tuple(moves)))

    def _possible_takes(self,
                        board,
                        cur_pos: Position,
                        allows=(True, True, True, True)):
        moves = []

        allow_sw, allow_se, allow_nw, allow_ne = allows

        for pos in board.locations_around(cur_pos,
                                          single=True,
                                          allow_down=False,
                                          allow_up=False,
                                          allow_sw=allow_sw,
                                          allow_se=allow_se,
                                          allow_nw=allow_nw,
                                          allow_ne=allow_ne):
            if not board.is_field_empty(
                    pos) and board.field_at(pos).figure.owner != self.owner:
                width_diff, height_diff = pos.diff(cur_pos)

                allow_sw, allow_se, allow_nw, allow_ne = diff_to_allow(
                    width_diff, height_diff)

                for take_position in board.locations_around(pos,
                                                            single=False,
                                                            allow_down=False,
                                                            allow_up=False,
                                                            allow_sw=allow_sw,
                                                            allow_se=allow_se,
                                                            allow_nw=allow_nw,
                                                            allow_ne=allow_ne):
                    if board.is_field_empty(take_position):
                        moves.append(
                            TreeNode(
                                take_position,
                                taking=pos,
                                children=self._possible_takes(
                                    board,
                                    take_position,
                                    allows=negate_allows(*invert_single_allow(
                                        allow_sw, allow_se, allow_nw,
                                        allow_ne)))))

        return tuple(moves)

    def __repr__(self):
        return f'King(color: {self.color}, owner: {self.owner})'
