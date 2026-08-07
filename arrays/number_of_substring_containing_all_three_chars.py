def main(arr):
    ans = 0
    l=0
    freq = {'a':0, 'b': 0, 'c': 0}
    for r in range(len(arr)):
        freq[arr[r]]+=1
        while freq['a']>0 and freq['b']>0 and freq['c']>0:
            ans+=len(arr)-r
            freq[arr[l]]-=1
            l+=1
    return ans