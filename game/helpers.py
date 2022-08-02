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


def diff_to_allow(width_diff, height_diff):
    allow_se = False
    allow_sw = False
    allow_ne = False
    allow_nw = False

    if width_diff < 0 and height_diff < 0:
        allow_nw = True
    if width_diff < 0 and height_diff > 0:
        allow_ne = True
    if width_diff > 0 and height_diff < 0:
        allow_sw = True
    if width_diff > 0 and height_diff > 0:
        allow_se = True

    return allow_sw, allow_se, allow_nw, allow_ne


def allow_to_diff(allow_sw, allow_se, allow_nw, allow_ne):
    if allow_nw:
        width_diff = -1
        height_diff = -1
    if allow_ne:
        width_diff = -1
        height_diff = 1
    elif allow_sw:
        width_diff = 1
        height_diff = -1
    elif allow_se:
        width_diff = 1
        height_diff = 1

    return width_diff, height_diff


def invert_single_allow(allow_sw, allow_se, allow_nw, allow_ne):
    width_diff, height_diff = allow_to_diff(allow_sw, allow_se, allow_nw,
                                            allow_ne)
    return diff_to_allow(width_diff * -1, height_diff * -1)


def negate_allows(allow_sw, allow_se, allow_nw, allow_ne):
    return not allow_sw, not allow_se, not allow_nw, not allow_ne
