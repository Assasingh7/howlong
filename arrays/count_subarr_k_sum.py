def main(arr, k):
    pref_sum = {}
    pref_sum[0] = 1
    summ = 0
    cnt = 0
    for i in range(len(arr)):
        summ+=arr[i]
        remaiin = pref_sum[summ] - k
        if remaiin in pref_sum:
            cnt+=pref_sum[remaiin]
        pref_sum[remaiin] = pref_sum.get(remaiin, 0)+1
    return cnt
