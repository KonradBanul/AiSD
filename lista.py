from typing import Any

class Node:
    value: Any
    next: 'Node'

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value: Any)->None:
        node = Node(value)
        node.next = self.head
        self.head = node

    def node(self, at: int)->None:
        current = self.head
        while(at > 0):
            current = current.next
            at -= 1
        return current.value

list_ = LinkedList()
assert list_.head == None
list_.push(1)
list_.push(10)
print(list_.node(0))
print(list_.node(1))



