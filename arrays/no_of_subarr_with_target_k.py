def main(arr, k):
    cnt = 0
    l = 0
    for r in range(len(arr)):
        # summ  = 0
        summ = sum(arr[l:r+1])
        if summ == k:
            cnt+=1
        if summ>0:
            summ-=arr[l]
            l+=1
    return cnt
print(main([1, 0, 0, 1, 1, 0], 2))