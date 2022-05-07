from game.tree.TreeNode import TreeNode


class Tree:
    def __init__(self, root_node: TreeNode):
        assert root_node is not None, "Root can't be None"

        self._root_node = root_node

    @property
    def root(self):
        return self._root_node

