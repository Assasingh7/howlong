from collections import deque
def main(src, adj, vis):
    vis[src] = 1
    q = deque()
    q.append((src, -1))
    while q:
        node, parent = q.popleft()
        for adjNode in adj[node]:
            if not vis[adjNode]:
                vis[adjNode] = 1
                q.append((adjNode, node))
            elif parent!=adjNode:
                return True
    return False


