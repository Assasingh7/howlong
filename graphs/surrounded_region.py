from collections import deque
def main(grid):
    n = len(grid)
    m = len(grid[0])
    q = deque()
    for i in range(n):
        for j in range(m):
            if i==0 or i==n-1 or j==0 or j==m-1:
                if grid[i][j] == 'O':
                      grid[i][j] == '#'
                      q.append((i, j))
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nrow = r+dr
            ncol = c+dc
            if nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol] == 'O':
                grid[nrow][ncol] = '#'
                q.append((nrow, ncol))
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'O':
                grid[i][j] = 'X' 
            if grid[i][j] == '#':
                grid[i][j] = 'O'
