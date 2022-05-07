from .figure import Figure
from .color import Color
from .tree.Tree import Tree
from .tree.TreeNode import TreeNode


class Man(Figure):
    def __init__(self, owner):
        super().__init__(owner)

    # TODO: represent moves as tree object
    # TODO: get possible moves
    def possible_moves(self, board):
        cur_pos = board.location(self)
        j, i = cur_pos

        moves = []

        allow_up = self.color == Color.WHITE
        allow_down = self.color == Color.BLACK

        for field, pos in board.locations_around(cur_pos, allow_up=allow_up, allow_down=allow_down):
            if board.is_field_empty(pos):
                moves.append(TreeNode(pos))
            elif board.field_at_indexes(pos).figure.owner != self.owner:
                diff = (pos[0] - cur_pos[0], pos[1] - cur_pos[1])
                take_position = (pos[0] + diff[0], pos[1] + diff[1])

                if board.is_field_empty(take_position):
                    moves.append(TreeNode(take_position, self.moves(board, take_position)))

        return Tree(TreeNode(cur_pos, tuple(moves)))

        # if self.color == Color.WHITE:
        #     # Cannot move forward
        #     from game.board import Board
        #     if j > Board.BOARD_SIZE - 2:
        #         return []
        #     # NORTH WEST (from board pretty_print view)
        #     if i > 0:
        #         if not board.field_at_indexes((i - 1, j + 1)).figure:
        #             moves.append((i - 1, j + 1))
        #     # NORTH EAST (from board pretty_print view)
        #     if i < Board.BOARD_SIZE - 2:
        #         if not board.field_at_indexes((i + 1, j + 1)).figure:
        #             moves.append((i + 1, j + 1))
        # else:
        #     # Cannot move forward
        #     if j < 1:
        #         return []
        #     # SOUTH WEST (from board pretty_print view)
        #     if i > 0:
        #         if not board.field_at_indexes((i - 1, j - 1)).figure:
        #             moves.append((i - 1, j - 1))
        #     # SOUTH EAST (from board pretty_print view)
        #     if i < Board.BOARD_SIZE - 2:
        #         if not board.field_at_indexes((i + 1, j - 1)).figure:
        #             moves.append((i + 1, j - 1))
        # return moves

    def moves(self, board, cur_pos, allow_up, allow_down):
        moves = []

        for field, pos in board.locations_around(cur_pos, allow_up=allow_up, allow_down=allow_down):
            if not board.is_field_empty(pos) and board.field_at_indexes(pos).owner != self.owner:
                diff = (pos[0] - cur_pos[0], pos[1] - cur_pos[1])
                take_position = (pos[0] + diff[0], pos[1] + diff[1])

                if board.is_field_empty(take_position):
                    moves.append(TreeNode(take_position, self.moves(board, take_position, allow_up, allow_down)))

        return tuple(moves)

    def __repr__(self):
        return f'Man(color: {self.color}, owner: {self.owner})'
