def main(n, dp):
    if n==1 or n==0:
        return 1
    if dp[n]!=-1:
        return dp[n]
    one = main(n-1, dp)
    two = main(n-2, dp)
    dp[n]=one+two
    return dp[n]

dp = [-1]*4
def main_bottom(n):
    dp = [-1]*(n+1)
    dp[0] = dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]
print(main_bottom(3))