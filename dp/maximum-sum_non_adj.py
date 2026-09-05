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
class Solution:
    # Function to return maximum sum of non-adjacent elements
    def maximumNonAdjacentSum(self, arr):
        # Get size of array
        n = len(arr)

        # If array has one element
        if n == 1:
            return arr[0]

        # Initialize dp array
        dp = [0] * n

        # Base cases
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])

        # Iterate from 3rd element
        for i in range(2, n):
            # Pick current + dp[i-2] or skip current
            dp[i] = max(arr[i] + dp[i - 2], dp[i - 1])

        # Final result at last index
        return dp[n - 1]


# Driver code
arr = [2, 1, 4, 9]
sol = Solution()
print(sol.maximumNonAdjacentSum(arr))
