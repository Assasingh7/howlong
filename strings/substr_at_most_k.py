def main(s, k):
    left, res = 0, 0
    mpp = {}
    for r in range(len(s)):
        mpp[s[r]] = mpp.get(s[r], 0)+1
        while len(mpp)>k:
            mpp[s[left]]-=1
            if mpp[s[left]] == 0:
                del mpp[s[left]]
            left+=1
        res+=(r-left+1)
    return res
print(main("pqpqs", 2)-main("pqpqs", 1))