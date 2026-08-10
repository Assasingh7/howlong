from collections import defaultdict, deque
class Tree:
    def __init__(self, data):
        self.data  = data
        self.left=None
        self.right = None
def main(root):
    res = []
    q = deque()
    q.append((root, 0))
    mapp = defaultdict(int)
    while q:
        size = len(q)
        # level = []
        for i in range(size):
            node, HD = q.popleft()
            if HD not in mapp:
                mapp[HD] = node.data
            if node.left:
                q.append((node.left, HD-1))
            if node.right:
                q.append((node.right, HD+1))
    for i in sorted(mapp):
        res.append(mapp[i])
    return res
        