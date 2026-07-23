def main(arr):
    m = len(arr)
    n = len(arr[0])
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                for q in range(n):
                    if arr[i][q]!= 0:
                        arr[i][q] = -1
                for l in range(m):
                    if arr[l][j]!= 0:
                        arr[l][j] = -1
    for i in range(m):
        for j in range(n):
            if arr[i][j] == -1:
                arr[i][j] = 0
    return arr

def mmain(arr):
    m = len(arr)
    n = len(arr[0])
    row = [0]*m
    col = [0]*n
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                row[i] = 1
                col[j] = 1
    
    for i in range(m):
        for j in range(n):
            if row[i] == 1 or col[j] == 1:
                arr[i][j] = 0
    return arr
def main_op(matrix):
    m = len(matrix)
    n = len(matrix[0])
    first_row_zero = False
    first_col_zero = False
    for i in range(m):
        if matrix[0][i] == 0:
            first_row_zero = True
            break
    for i in range(n):
        if matrix[i][0] == 0:
            first_col_zero = True
            break
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0

    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0
    return matrix
print(main_op([[1,1,1],[1,0,1],[1,1,1]]))