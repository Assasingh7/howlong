class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def main(root):
    if root == None:
        return 0
    left = main(root.left)
    if left == -1:
        return -1
    right = main(root.right)
    if right == -1:
        return -1
    if abs(left-right)>1:
        return -1
    return 1+max(left, right)