class MinStack:
    def __init__(self):
        self.st = []
        self.mst = []
    def push(self, x):
        self.st.append(x)
        if not self.mst or x<=self.mst[-1]:
            self.mst.append(x)
    def pop(self):
        val = self.st.pop()
        if val == self.mst[-1]:
            self.mst.pop()
        return val
    def peek(self):
        return self.st[-1] if self.st else None
    def get_min(self):
        return self.mst[-1]