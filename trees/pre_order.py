class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def main(root, arr):
    if root is None:
        return None
    arr.append(root.data)
    main(root.left, arr)
    main(root.right, arr)
