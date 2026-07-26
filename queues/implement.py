class Queue:
    def __init__(self, size):
        self.arr = [0]*size
        self.size = size
        self.front = 0
        self.rear = -1
        self.count = 0
    def enqueue(self, el):
        if self.is_full():
            print("Queue Full")
            return
        self.rear = (self.rear+1) % self.size
        self.arr[self.rear] = el
        self.count+=1
    def dequeue(self):
        if self.is_empty():
            print("Queue Empty")
            return
        value = self.arr[self.front]
        self.front = (self.front+1) % self.size
        self.count-=1
        return value
    def peek(self):
        return self.arr[self.front]
    def is_empty(self):
        return self.count == 0
    def is_full(self):
        return self.count == self.size