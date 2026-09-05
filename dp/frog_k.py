def main(ind, height, k, dp):
    if ind==0:
        return 0
    if dp[ind]!=-1:
        return dp[ind]
    mmsteps = float('inf')
    for j in range(1, k+1):
        if ind-j>=0:
            jump = abs(height[ind]-height[ind-j])+main(ind-j, height, k, dp)
            mmsteps = min(mmsteps, jump)
    dp[ind] = mmsteps
    return dp[ind]
class Solution:
    # Function to compute the minimum cost to reach the end using at most 'k' jumps
    def solveUtil(self, n, height, dp, k):
        # Base case: cost to reach first stone is 0
        dp[0] = 0

        # Iterate over each stone
        for i in range(1, n):
            # Initialize minimum cost for this stone as large value
            mmSteps = float('inf')

            # Try all possible jump lengths from 1 to k
            for j in range(1, k + 1):
                # Ensure jump doesn't go out of bounds
                if i - j >= 0:
                    # Cost of jumping from (i - j) to i
                    jump = dp[i - j] + abs(height[i] - height[i - j])
                    # Keep track of the minimum cost
                    mmSteps = min(mmSteps, jump)

            # Store computed minimum cost
            dp[i] = mmSteps

        # Last element of dp stores the answer
        return dp[n - 1]

    # Function to solve the problem
    def solve(self, n, height, k):
        # Initialize DP array with -1
        dp = [-1] * n
        return self.solveUtil(n, height, dp, k)

# Driver code
if __name__ == "__main__":
    # Heights of stones
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    k = 2

    # Create solution object
    sol = Solution()

    # Output result
    print(sol.solve(n, height, k))
