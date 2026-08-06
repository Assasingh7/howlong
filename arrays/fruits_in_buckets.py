def main(arr):
    freq = {}
    l = 0
    ans = 0
    for r in range(len(arr)):
        freq[arr[r]]+=1
        while len(freq)>2:
            if freq[arr[l]]==0:
                del freq[arr[l]]
            l+=1
        ans = max(ans, r-l+1)
    return ans
