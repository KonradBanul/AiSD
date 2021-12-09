from typing import Any


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_leaf(self):
        if self.left_child is None and self.right_child is None:
            return True
        return False

    def add_left_child(self, value):
        if self.left_child is None:
            self.left_child = BinaryNode(value)

    def add_right_child(self, value):
        if self.right_child is None:
            self.right_child = BinaryNode(value)

    def visit(self):
        return self.value

    def traverse_pre_order(self):
        print(self.visit())
        if self.left_child is not None:
            self.left_child.traverse_pre_order()
        if self.right_child is not None:
            self.right_child.traverse_pre_order()

    def traverse_in_order(self):
        if self.left_child is not None:
            self.left_child.traverse_in_order()
        print(self.visit())
        if self.right_child is not None:
            self.right_child.traverse_in_order()

    def traverse_post_order(self):
        if self.left_child is not None:
            self.left_child.traverse_post_order()
        if self.right_child is not None:
            self.right_child.traverse_post_order()
        print(self.visit())


class BinaryTree:
    root: BinaryNode

    def __init__(self, value) -> None:
        self.value = value
        self.root = BinaryNode(value)

    def add_left_child(self, value):
        self.root.add_left_child(value)

    def add_right_child(self, value):
        self.root.add_right_child(value)

    def traverse_in_order(self):
        self.root.traverse_in_order()

    def traverse_pre_order(self):
        self.root.traverse_pre_order()

    def traverse_post_order(self):
        self.root.traverse_post_order()


def all_equal_paths(tree, sum_value):
    wynik1 = []
    wynik2 = []
    wynik3 = []
    wynik4 = []
    if tree.root.value + tree.root.left_child.value + tree.root.left_child.left_child.value == sum_value:
        wynik1.append(tree.root.value)
        wynik1.append(tree.root.left_child.value)
        wynik1.append(tree.root.left_child.left_child.value)
        print(wynik1)
    if tree.root.value + tree.root.left_child.value + tree.root.left_child.right_child.value == sum_value:
        wynik2.append(tree.root.value)
        wynik2.append(tree.root.left_child.value)
        wynik2.append(tree.root.left_child.right_child.value)
        print(wynik2)
    if tree.root.value + tree.root.right_child.value + tree.root.right_child.left_child.value == sum_value:
        wynik3.append(tree.root.value)
        wynik3.append(tree.root.right_child.value)
        wynik3.append(tree.root.right_child.left_child.value)
        print(wynik3)
    if tree.root.value + tree.root.right_child.value + tree.root.left_child.right_child.value == sum_value:
        wynik4.append(tree.root.value)
        wynik4.append(tree.root.right_child.value)
        wynik4.append(tree.root.right_child.right_child.value)
        print(wynik4)


tree = BinaryTree(10)
assert tree.root.value == 10
tree.add_left_child(9)
tree.add_right_child(2)
assert tree.root.right_child.value == 2
tree.root.left_child.add_left_child(1)
tree.root.left_child.add_right_child(3)
tree.root.right_child.add_left_child(4)
tree.root.right_child.add_right_child(6)
assert tree.root.left_child.left_child.value == 1
assert tree.root.right_child.is_leaf() is False
assert tree.root.left_child.left_child.is_leaf() is True
tree.traverse_in_order()
print("**********************")
tree.traverse_post_order()
print("**********************")
tree.traverse_pre_order()
print("**********************")
print(all_equal_paths(tree, 20))
