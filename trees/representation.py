class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# for arr [1, 2, 3, 4, 5], left  = 2*i+1  right = 2*i+2 parent = (i-1)//2