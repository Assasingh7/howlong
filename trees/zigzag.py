from collections import deque
def main(root):
    res = []
    queue = deque([root.val])
    leftToRight = True
    while queue:
        size = len(queue)
        
        level = [0]*size
        for i in range(size):
            node = queue.popleft()
            index=i if leftToRight else size-1-i
            level[index] = node
            if node.left:
                queue.append(node.left.val)
            if node.right:
                queue.append(node.right.val)
        leftToRight = not leftToRight
        res.append(level)
    return res
