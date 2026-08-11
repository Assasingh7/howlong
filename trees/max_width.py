from collections import deque

def main(root):
    q= deque()
    max_width = 0
    q.append((root, 0))

    while q:
        last = None
        size = len(q)
        first = q[0][1]
        for i in range(size):
            node, index = q.popleft()
            if i == size-1:
                last = index
            if node.left:
                q.append((node.left, 2*index+1))
            if node.right:
                q.append((node.right, 2*index+2))
        width = last-first+1
        max_width = max(max_width, width)
    return max_width