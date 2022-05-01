from .figure import Figure
from .color import Color

class Man(Figure):

    # TODO: represent moves as tree object
    # TODO: get possible moves
    def possible_moves(self, board, pos_index=None):
        if not pos_index:
            i, j = self.get_index()
        else:
            i, j = pos_index
        color = self.get_color()

        moves = []
        if color == Color.WHITE:
            # Cannot move forward
            if j > board.get_size() - 2:
                return []
            # SOUTH WEST (from board pretty_print view)
            if i > 0:
                if not board.get_field_at_index( (i-1, j+1) ).get_figure():
                    moves.append( (i-1, j+1) )
            # SOUTH EAST (from board pretty_print view)
            if i < board.get_size() - 2:
                if not board.get_field_at_index( (i+1, j+1) ).get_figure():
                    moves.append( (i+1, j+1) )
        elif color == Color.BLACK:
            # Cannot move forward
            if j < 1:
                return []
            # NORTH WEST (from board pretty_print view)
            if i > 0:
                if not board.get_field_at_index( (i-1, j-1) ).get_figure():
                    moves.append( (i-1, j-1) )
            # NORTH EAST (from board pretty_print view)
            if i < board.get_size() - 2:
                if not board.get_field_at_index( (i+1, j-1) ).get_figure():
                    moves.append( (i+1, j-1) )
        return moves
