def main(s):
    n = len(s)
    max_len = 0
    for i in range(n):
        hash_arr = [0]*n
        for j in range(i, n):
            if hash_arr[ord(s[j])] in hash_arr:
                break
            hash_arr[ord(s[j])] = 1
            max_len = max(max_len, j-i+1)
    return max_len
def mainn(s):
    n = len(s)
    hash_arr = [-1]* 256
    l, r, max_sum = 0, 0, 0
    while r<n:
        if hash_arr[ord[s[r]]] != -1:
            l = max(l, hash_arr[ord[s[r]]+1])
        cur = r-l+1
        max_sum = max(max_sum, cur)
        hash_arr[s[r]] = r
        r+=1
    return max_sum
    


