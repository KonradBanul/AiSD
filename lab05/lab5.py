from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_leaf(self):
        if self.left_child is None or self.right_child is None:
            return True
        else:
            return False

    def add_left_child(self, value):
        if self.left_child is None:
            self.left_child = BinaryNode(value)

    def add_right_child(self, value):
        if self.right_child is None:
            self.right_child = BinaryNode(value)

    def visit(self, node):
        print(node.value)

    def traverse_post_order(self, visit):
        if self.left_child is not None:
            self.traverse_post_order(visit)
        elif self.right_child is not None:
            self.traverse_post_order(visit)


class BinaryTree:
    root: BinaryNode

    def __init__(self, value):
        self.root = BinaryNode(value)


tree = BinaryTree(10)
assert tree.root.value == 10
tree.root.add_right_child(2)
assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is True
tree.root.add_left_child(9)
tree.root.add_left_child(1)
