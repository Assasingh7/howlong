from collections import deque
def main(graph, n):
    indegree = [0]*n
    queue = deque()
    for i in range(n):
        for node in graph[i]:
            indegree[node]+=1
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
    res = []
    while queue:
        nodee = queue.popleft()
        res.append(nodee)
        for n in graph[nodee]:
            indegree[n]-=1
            if indegree[n] == 0:
                queue.append(n)
    if len(res)!=n:
        return None
    return res

            
