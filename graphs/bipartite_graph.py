def dfs(node, col, color, adj):
    color[node] = col
    for it in adj[node]:
        if color[it] == -1:
            if dfs(it, 1 - col, color, adj) == False: return False
        elif color[it] == col:
            return False
    return True
