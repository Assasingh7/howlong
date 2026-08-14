from collections import deque
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def main(root, target, k):
    if not root:
        return []
    parent_map = {}
    create_map(root, parent_map)
    res = bfs_at_k(target, k, parent_map)
    return res
def create_map(root, parent_map):
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if node.left:
            parent_map[node.left] = node
            queue.append(node.left)
        if node.right:
            parent_map[node.right] = node
            queue.append(node.right)

def bfs_at_k(root, k, parent_map):
    queue = deque()
    queue.append(root)
    vis = set()
    vis.add(root)
    cur_level = 0
    while queue:
        size = len(queue)
        if cur_level == k:
            break
        for _ in range(size):
            node = queue.popleft()
            if node.left and node.left not in vis:
                queue.append(node.left)
                vis.add(node.left)
            if node.right and node.right not in vis:
                queue.append(node.right)
                vis.add(node.right)
            if node in parent_map and parent_map[node] not in vis:
                queue.append(parent_map[node])
                vis.add(parent_map[node])
        cur_level+=1
    return [node.val for node in queue]