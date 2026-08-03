class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def enqueue(self, x):
        new = Node(x)
        if self.head is None:
            self.head = new
            self.tail = new
            return
        self.tail.next = new
        self.tail = new
    def dequeue(self):
        if self.head is None:
            return "Empty "
        val = self.head.data
        self.head = self.head.next
        return val
    def empty(self):
        return self.head is None
    def peek(self):
        if self.head is None:
            return None
        return self.head.data