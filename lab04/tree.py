from queue import Queue


class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.children = []
        self.visit = True

    def is_leaf(self):
        if self.children is None:
            return True
        else:
            return False

    def add(self, child):
        self.children.append(child)

    def for_each_level_order(self):
        q = Queue()
        q.enqueue(self)
        while q.storage.head is not None:
            print(q.storage.head.data.value)
            for i in q.storage.head.data.children:
                q.enqueue(i)
            q.dequeue()

    def for_each_deep_first(self):
        print(self.value)
        for i in self.children:
            if i.visit is True:
                i.for_each_deep_first()


class Tree:
    def __init__(self, value):
        self.root = TreeNode(value)

    def for_each_level_order(self):
        self.root.for_each_level_order()

    def for_each_deep_first(self):
        self.root.for_each_deep_first()

    def add(self, value, parent_value):
        q = Queue()
        q.enqueue(self.root)
        if q.storage.head.data.value == parent_value:
            self.root.children.append(TreeNode(value))
            return None
        while q.storage.head is not None:
            for i in q.storage.head.data.children:
                if i.value == parent_value:
                    i.add(TreeNode(value))
                    return None
                q.enqueue(i)
            q.dequeue()


tree = TreeNode("F")
tree.add(TreeNode("B"))
tree.add(TreeNode("G"))
tree.children[0].add(TreeNode("A"))
tree.children[0].add(TreeNode("D"))
tree.children[1].add(TreeNode("I"))
tree.children[0].children[1].add(TreeNode("C"))
tree.children[0].children[1].add(TreeNode("E"))
tree.children[1].children[0].add(TreeNode("H"))
tree.for_each_deep_first()
print("----------")
tree.for_each_level_order()
print("----------")
tree = Tree("F")
tree.add("B", "F")
tree.add("G", "F")
tree.add("A", "B")
tree.add("D", "B")
tree.add("C", "D")
tree.add("E", "D")
tree.add("I", "G")
tree.add("H", "I")
tree.for_each_deep_first()
print("----------")
tree.for_each_level_order()
