from queue import Queue
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def main(root):
    if root == None:
        return 0
    return 1+max(main(root.left), main(root.right))
def mainn(root):
    q = Queue()
    level = 0
    q.put(root)
    while not q.empty():
        size = q.qsize()
        for i in range(size):
            node = q.get()
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        level+=1
    return level
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(7)

print(mainn(root))