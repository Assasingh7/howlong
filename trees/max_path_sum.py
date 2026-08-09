maxxx = float('-inf')
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def main(root):
    global maxxx
    if root is None:
        return 0
    left = main(root.left)
    right = main(root.right)
    max_sum = root.data+max(0, left, right)
    path = root.data+max(0, left)+max(0, right)
    maxxx=max(path, maxxx)
    return max_sum