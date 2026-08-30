from collections import deque
def main(grid, source, destination):
    if source == destination:
        return 0
    n = len(grid)
    m = len(grid[0])
    dist = [float('inf')*m for _ in range(n)]
    dist[source[0]][source[1]] = 0
    q = deque([(0, source[0], source[1])])
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, 0, -1]
    while q:
        dis, r, c = q.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0<=nr<n and 0<=nc<m and grid[nr][nc]== 1 and dis+1<dist[nr][nc]:
                dist[nr][nc] = dis+1
                if (nr, nc) == destination:
                    return dis+1
                q.append((dis+1, nr, nc))
    return -1