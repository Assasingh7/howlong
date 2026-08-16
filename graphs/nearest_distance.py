from collections import deque
def main(arr):
    n=len(arr)
    m=len(arr[0])
    dist=[[-1]*m for _ in range(n)]
    queue = deque()
    for i in range(n):
        for j in range(m):
            queue.append((i, j))
            dist[i, j] = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nrow = r+dr
            ncol = c+dc
            if nrow>=0 and nrow<n and ncol>=0 and ncol<m and dist[nrow][ncol] == -1:
                dist[nrow][ncol] = dist[r][c]+1
                queue.append((nrow, ncol))
    return dist
