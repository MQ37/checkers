from .figure import Figure
from .color import Color
from .position import Position
from .tree.Tree import Tree
from .tree.TreeNode import TreeNode


class Man(Figure):

    def __init__(self, owner):
        super().__init__(owner)

    # TODO: represent moves as tree object
    # TODO: get possible moves
    def possible_moves(self, board) -> Tree:
        cur_pos: Position = board.location(self)

        moves = []

        allow_up = self.color is Color.WHITE
        allow_down = self.color is Color.BLACK

        for pos in board.locations_around(cur_pos,
                                          allow_up=allow_up,
                                          allow_down=allow_down):
            if board.is_field_empty(pos):
                moves.append(TreeNode(pos))
            elif board.field_at(pos).figure.owner != self.owner:
                width_diff, height_diff = pos.diff(cur_pos)

                # TODO: add check if at the end of the board
                row, col = pos.tuple
                row_diff = width_diff
                col_diff = height_diff

                take_row = row + row_diff
                take_col = col + col_diff
                if take_row < 0 or take_row > board.BOARD_SIZE - 1:
                    continue
                if take_col < 0 or take_col > board.BOARD_SIZE - 1:
                    continue
                take_position = pos.move(width_diff, height_diff)

                if board.is_field_empty(take_position):
                    moves.append(
                        TreeNode(take_position,
                                 self.moves(board, take_position, allow_up,
                                            allow_down),
                                 taking=pos))

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

    def moves(self, board, cur_pos: Position, allow_up, allow_down):
        moves = []

        for pos in board.locations_around(cur_pos,
                                          allow_up=allow_up,
                                          allow_down=allow_down):
            if not board.is_field_empty(
                    pos) and board.field_at(pos).figure.owner != self.owner:
                width_diff, height_diff = pos.diff(cur_pos)

                # TODO: add check if at the end of the board
                row, col = pos.tuple
                row_diff = width_diff
                col_diff = height_diff

                take_row = row + row_diff
                take_col = col + col_diff
                if take_row < 0 or take_row > board.BOARD_SIZE - 1:
                    continue
                if take_col < 0 or take_col > board.BOARD_SIZE - 1:
                    continue

                take_position = pos.move(width_diff, height_diff)

                if board.is_field_empty(take_position):
                    moves.append(
                        TreeNode(take_position,
                                 self.moves(board, take_position, allow_up,
                                            allow_down),
                                 taking=pos))

        return tuple(moves)

    def __repr__(self):
        return f'Man(color: {self.color}, owner: {self.owner})'
