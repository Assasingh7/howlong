def main(arr, k):
    l = 0
    ans = 0
    fre_map = {}
    for r in range(len(arr)):
        fre_map[arr[r]]+=1
        max_freq = max(max_freq, fre_map[arr[r]])
        while (r-l+1)-max_freq>k:
            fre_map[arr[l]]-=1
            l-=1
        ans = max(ans, r-l+1)
    return ans