def main(arr, i, j, vis, idx, s):
    n = len(arr)
    m = len(arr[0])
    if idx == len(s):
        return True
    if i<0 or j<0 or i>n-1 or j>m-1 or vis[i][j] == 1 or arr[i][j]!=s[idx]:
        return False
    vis[i][j] = 1
    found = main(arr, i-1, j, vis, idx+1, s) or main(arr, i, j-1, vis, idx+1, s) or main(arr, i+1, j, vis, idx+1, s) or main(arr, i, j+1, vis, idx+1, s)
    vis[i][j] = 0
    return found

def mainn(arr, i, j, idx, s):
    n = len(arr)
    m = len(arr[0])
    if idx == len(s):
        return True
    if i<0 or j<0 or i>n-1 or j>m-1 or arr[i][j]!=s[idx]:
        return False
    temp = arr[i][j]
    arr[i][j] = '#'
    found = main(arr, i-1, j, idx+1, s) or main(arr, i, j-1, idx+1, s) or main(arr, i+1, j, idx+1, s) or main(arr, i, j+1, idx+1, s)
    arr[i][j] = temp
    return found