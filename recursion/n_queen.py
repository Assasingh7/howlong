def main(board,  j, ans, k):
    m = len(board[0])
    if j == m:
        temp = [''.join(row) for row in board]
        ans.append(temp)
        return ans
    for i in range(k):
        if is_safe(board, i, j):
            board[i][j] = 'Q'
            main(board,  j+1, ans, k)
            board[i][j] = '.'
    return ans

def is_safe(board, i, j):
    for col in range(j):
        if board[i][col] == 'Q':
            return False
    r, c = i, j
    while r>=0 and c>=0:
        if board[r][c] == 'Q':
            return False
        r-=1
        c-=1
    r, c = i, j
    while r<len(board) and c>=0:
        if board[r][c] == 'Q':
            return False
        r+=1
        c-=1
    return True
n = 4
board = [['.' for _ in range(n)] for _ in range(n)]
print(main(board, 0, [], k=4))