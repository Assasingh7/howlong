class Stack:
    # stk = []
    def __init__(self):
        self.stk = []
        # self.x  = x
        self.top_index = -1
        
    def push(self, x):
        self.stk.append(x)
        self.top_index +=1
    def peek(self):
        return self.stk[self.top_index] if self.top_index>-1 else None
    def pop(self):
        if self.top_index == -1:
            return None
        self.top_index -= 1
        return self.stk.pop()
    def empty(self):
        return self.top_index == -1


