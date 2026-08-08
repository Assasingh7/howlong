def atmostK(arr, k):
    ans = 0
    l = 0
    freq = {}
    for r in range(len(arr)):
        if arr[r] not in freq or freq[arr[r]]==0:
            k-=1
        freq[arr[r]]+=1
        while k<0:
            freq[arr[l]]-=1
            if k == 0:
                k+=1
            l+=1
        ans+=(r-l+1)
    return ans