from collections import deque
def main(v, adj):
    queue = deque()
    vis = [False]*v
    res = []
    queue.append(0)
    vis[0] = True
    while queue:
        node = queue.popleft()
        res.append(node)
        for n in adj[node]:
            if not vis[n]:
                vis[n] = True
                queue.append(n)
    return res

v= 5
adj = [[] for _ in range(v)]
adj[0] = [1, 2]
adj[1] = [0, 3]
adj[2] = [0, 4]
adj[3] = [1]
adj[4] = [2]
print(main(5, adj))