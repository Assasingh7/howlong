def dfs(row, col, base_row, base_col, grid, vis, shape):
    vis[row][col] = True
    shape.append((row - base_row, col - base_col))
    drow = [-1, 0, 1, 0]
    dcol = [0, 1, 0, -1]
    for i in range(4):
        nr = row + drow[i]
        nc = col + dcol[i]
        if (0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==1 and not vis[nr][nc]):
            dfs(nr, nc, base_row, base_col, grid, vis, shape)
def main(grid):
    n, m = len(grid), len(grid[0])
    vis = [[False for _ in range(m)] for _ in range(n)]
    st = set()
    for i in range(n):
        for j in range(m):
            if not vis[i][j] and grid[i][j] == 1:
                shape = []
                dfs(i, j, i, j, grid, vis, shape)
                st.add(tuple(shape))
    return len(shape)
