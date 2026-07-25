def main(arr, res, i, j, s, vis):
    n = len(arr)
    m = len(arr[0])
    if i<0 or j<0 or i>n-1 or j>m-1 or vis[i][j] or arr[i][j]!=1 :
        return False
    if i==n-1 and j==m-1:
        res.append(s)
        return
    vis[i][j] = True
    main(arr, res, i-1, j, s+'U', vis)
    main(arr, res, i, j-1, s+'L', vis)
    main(arr, res, i, j+1, s+'R', vis)
    main(arr, res, i+1, j, s+'D', vis)
    vis[i][j] = False
    return
