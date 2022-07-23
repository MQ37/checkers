from .coord_map import COORD_MAP_L, COORD_MAP_R
from .color import Color

BOARD_SIZE = 8
CORRECT_NOTATION_REGEX = r'^([A-H])([1-8])$'


# coords -> (str, int) | ("A", 1) or str | "A1"
def get_color_by_coords(coords):
    r, c = coords
    # for "A1" coords format
    c = int(c)
    ir = COORD_MAP_L[r]

    if ir % 2 == 1 and c % 2 == 0:
        return Color.BLACK
    elif ir % 2 == 0 and c % 2 == 1:
        return Color.BLACK
    else:
        return Color.WHITE


def index_to_coords(pos):
    r, c = pos
    cr = COORD_MAP_R[r + 1]
    return (cr, c + 1)


# coords -> (str, int) | ("A", 1) or str | "A1"
def coords_to_index(coords):
    r, c = coords
    # for "A1" coords format
    c = int(c)
    ir = COORD_MAP_L[r]
    return (ir - 1, c - 1)
