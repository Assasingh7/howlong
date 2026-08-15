from collections import deque
def main(grid):
    if not grid:
        return 0
    queue = deque()
    n = len(grid)
    m = len(grid[0])
    fresh_count = 0
    max_time = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
            elif grid[i][j]==1:
                fresh_count+=1
    if fresh_count == 0:
        return 0
    directions = [(-1, 0), (0, 1,), (1, 0), (0, -1)]
    while queue:
        r, c, time = queue.popleft()
        max_time = max(max_time, time)
        for dr, dc in directions:
            nrow = r+dr
            ncol = c+dc
            if nrow>=0 and ncol>=0 and nrow<n and ncol<m and grid[nrow][ncol] == 1:
                grid[nrow][ncol] = 2
                fresh_count-=1
                queue.append((nrow, ncol, time+1))
    return max_time if fresh_count == 0 else -1

    