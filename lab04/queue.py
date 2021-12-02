from typing import Any


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value: Any) -> None:
        if self.head is None:
            self.head = Node(value)
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = Node(value)

    def pop(self) -> Any:
        node = self.head
        self.head = node.next
        return node


class Queue:
    def __init__(self) -> None:
        self.storage = LinkedList()

    def enqueue(self, data) -> None:
        self.storage.append(data)

    def dequeue(self) -> None:
        temp = self.storage.head
        self.storage.pop()
        return temp
