from game.position import Position


class TreeNode:

    def __init__(self, value, children=(), taking=None):
        assert isinstance(children, tuple)
        assert value is not None and isinstance(
            value, Position), "Value can't be None"

        self._value = value
        self._children = children
        self._taking = taking

    @property
    def children(self):
        return self._children

    @property
    def value(self) -> Position:
        return self._value

    @property
    def taking(self) -> Position:
        return self._taking

    def __getitem__(self, idx):
        assert isinstance(idx, int) and 0 <= idx < len(
            self), f'Incorrect index (idx: {idx}, length: {len(self)})'

        return self._children[idx]

    def __len__(self) -> int:
        return len(self._children)

    def __repr__(self):
        return f'Node(value: {self.value}, children=({",".join(map(repr, self.children))}))'
