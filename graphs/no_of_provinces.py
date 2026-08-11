def dfs(node, adj, vis):
    vis[node]=True
    for i in adj[node]:
        if not vis:
            dfs(i, adj, vis)
def main(adj, V):
    adj_list = [[] for _ in range(V)]
    for i in range(V):
        for j in range(V):
            if adj[i][j] == 1 and i != j:
                adj_list[i].append(j)
                adj_list[j].append(i)
    visited = [False] * V   
    cnt = 0
    for i in range(V):
        if not visited[i]:
           cnt+=1
           dfs(i, adj, visited)
    return cnt