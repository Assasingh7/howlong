class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    def push(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new
    def pop(self):
        val = self.head.data
        self.head = self.head.next
        return val
    def top(self):
        return self.head.data
    def empty(self):
        return self.head is None