def main(i, arr, dp):
    if i<0:
        return 0
    if i==0:
        return arr[0]
    if dp[i]!=-1:
        return dp[i]
    pick = arr[i] + main(i-2, arr, dp)
    not_pick = main(i-1, arr, dp)
    dp[i] = max(pick, not_pick)
    return dp[i]
