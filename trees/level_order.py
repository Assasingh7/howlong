from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def main(root):
    queue = deque([root])
    ans = []
    while queue:
        # node  = queue.pop()
        level = []
        for _ in range(len(queue)):
            node  = queue.popleft()
            level.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans.append(level)
    return ans 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(main(root))