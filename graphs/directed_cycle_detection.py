from collections import deque
def isCycle(V, adj):
    indegree = [0]*[V]
    for u in indegree[V]:
        for v in adj[u]:
            indegree[v]+=1
    q = deque()
    for node in range[V]:
        if indegree[node] == 0:
            q.append(node)
    processed = 0
    while q:
        node = q.popleft()
        processed+=1
        for neighbour in adj[node]:
            indegree[neighbour]-=1
            if indegree[neighbour] == 0:
                q.append(neighbour)
    return processed!=V

