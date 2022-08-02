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

        directions = [
            {
                "allow_sw": True,
                "allow_se": False,
                "allow_nw": False,
                "allow_ne": False
            },
            {
                "allow_sw": False,
                "allow_se": True,
                "allow_nw": False,
                "allow_ne": False
            },
            {
                "allow_sw": False,
                "allow_se": False,
                "allow_nw": True,
                "allow_ne": False
            },
            {
                "allow_sw": False,
                "allow_se": False,
                "allow_nw": False,
                "allow_ne": True
            },
        ]
        for direction in directions:
            blocked = False
            for pos in board.locations_around(cur_pos,
                                              single=False,
                                              allow_down=False,
                                              allow_up=False,
                                              **direction):
                if board.is_field_empty(pos):
                    moves.append(TreeNode(pos))
                elif board.field_at(pos).figure.owner != self.owner:
                    allow_sw, allow_se, allow_nw, allow_ne = direction.values()

                    taking_only = False
                    for take_position in board.locations_around(
                            pos,
                            single=False,
                            allow_down=False,
                            allow_up=False,
                            **direction):
                        # If empty continue exploring
                        if board.is_field_empty(take_position):
                            taking, children = self._possible_takes(
                                board,
                                take_position,
                                allows=negate_allows(*invert_single_allow(
                                    allow_sw, allow_se, allow_nw, allow_ne)))

                            # Force taking
                            if not taking_only and taking:
                                # Discard all previous non taking moves
                                moves = []
                                taking_only = True
                            if not taking_only or (taking_only and taking):
                                moves.append(
                                    TreeNode(take_position,
                                             taking=pos,
                                             children=children))
                        # If blocked by figure stop
                        else:
                            blocked = True
                            break
                if blocked:
                    break

        return Tree(TreeNode(cur_pos, tuple(moves)))

    def _possible_takes(self,
                        board,
                        cur_pos: Position,
                        allows=(True, True, True, True)):
        moves = []
        ret_taking = False

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

                taking_only = False
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
                        if not ret_taking:
                            ret_taking = True
                        _taking, children = self._possible_takes(
                            board,
                            take_position,
                            allows=negate_allows(*invert_single_allow(
                                allow_sw, allow_se, allow_nw, allow_ne)))

                        # Force taking
                        if not taking_only and _taking:
                            # Discard all previous non taking moves
                            moves = []
                            taking_only = True
                        # Append taking only moves when taking moves exist
                        if not taking_only or (taking_only and _taking):
                            moves.append(
                                TreeNode(take_position,
                                         taking=pos,
                                         children=children))
                    # If blocked by figure stop
                    else:
                        break

        return ret_taking, tuple(moves)

    def __repr__(self):
        return f'King(color: {self.color}, owner: {self.owner})'
