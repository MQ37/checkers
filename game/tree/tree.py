from game.tree.tree_node import TreeNode


class Tree:

    def __init__(self, root_node: TreeNode):
        assert root_node is not None, "Root can't be None"

        self._root_node = root_node

    @property
    def root(self) -> TreeNode:
        return self._root_node

    def print_moves(self):
        for path in self.as_moves():
            print(" -> ".join(map(lambda pos: pos[0].notation, path)))

    def as_moves(self, split_taking=False):
        moves = []
        taking_moves = []

        def walk(node, path, taking=False):
            if len(node) == 0:
                if node.taking or taking:
                    taking_moves.append(path + [(node.value, node.taking)])
                else:
                    moves.append(path + [(node.value, node.taking)])
                return

            for child in node.children:
                walk(child,
                     path + [(node.value, node.taking)],
                     taking=taking or node.taking)

        walk(self.root, [])

        if split_taking:
            return moves, taking_moves
        else:
            return moves + taking_moves
