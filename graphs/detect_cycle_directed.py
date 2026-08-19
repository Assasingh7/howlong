def cycle(node, vis, pathvis, adj):
    vis[node] = 1
    pathvis[node] = 1
    for it in adj[node]:
        if not vis[it]:
            if cycle(it, vis, pathvis, adj) is True:
                return True
            elif pathvis[it] == 1:
                return True
    pathvis[node] = 0
    return False
