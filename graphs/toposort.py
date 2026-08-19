def main(graph, n):
    vis = [False]*n
    stack = []
    def dfs(node):
        vis[node] = True
        for n in graph[node]:
            if not vis[n]:
                dfs(n)
        stack.append(node)
    for i in range(n):
        if not vis[i]:
            dfs(i)
    return stack[::-1]