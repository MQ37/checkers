from .figure import Figure
from .color import Color


class Man(Figure):
    # TODO: represent moves as tree object
    # TODO: get possible moves
    def possible_moves(self, board):
        j, i = board.location(self)

        moves = []
        if self.color == Color.WHITE:
            # Cannot move forward
            from game.board import Board
            if j > Board.BOARD_SIZE - 2:
                return []
            # NORTH WEST (from board pretty_print view)
            if i > 0:
                if not board.field_at_indexes((i-1, j+1)).figure:
                    moves.append((i-1, j+1))
            # NORTH EAST (from board pretty_print view)
            if i < Board.BOARD_SIZE - 2:
                if not board.field_at_indexes((i+1, j+1)).figure:
                    moves.append((i+1, j+1))
        else:
            # Cannot move forward
            if j < 1:
                return []
            # SOUTH WEST (from board pretty_print view)
            if i > 0:
                if not board.field_at_indexes((i-1, j-1)).figure:
                    moves.append((i-1, j-1))
            # SOUTH EAST (from board pretty_print view)
            if i < Board.BOARD_SIZE - 2:
                if not board.field_at_indexes((i+1, j-1)).figure:
                    moves.append((i+1, j-1))
        return moves
