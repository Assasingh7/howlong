def main(v, adj, vis, res):
    vis[v] = True
    res.append(v)
    for i in adj[v]:
        if not vis[i]:
            main(i, adj, vis, res)

V = 5

adj = [[] for _ in range(V)]
adj[0] = [1, 2]
adj[1] = [0, 3]
adj[2] = [0, 4]
adj[3] = [1]
adj[4] = [2]
vis = [False]*V
res = []
main(0, adj, vis, res)
print(res)