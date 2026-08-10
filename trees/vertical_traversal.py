from collections import defaultdict, deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def main(root):
    res = []
    queue = deque()
    mapp = defaultdict(list)
    queue.append((root, 0, 0))
    while queue:
        node, row, col = queue.popleft()
        mapp[col].append((row, node.data))
        if node.left:
            queue.append((node.left, row+1, col-1))
        if node.right:
            queue.append((node.right, row+1, col+1))
    for col in sorted(mapp):
        mapp[col].sort()
        res.append([val for row, val in mapp[col]])
    return res
