def main(ind,height, dp):
    if not height:
        return 0
    if dp[ind]!=-1:
        return dp[ind]
    one_jump = main(ind-1, height, dp)+abs(height[ind]-height[ind-1])
    jump_two = float('-inf')
    if ind>1:
        jump_two = main(ind-2, height, dp)+abs(height[ind]-height[ind-2])
    dp[ind] = min(one_jump, jump_two)
    return dp[ind]

class Solution:
    # Computes minimum energy to reach last index using bottom-up DP
    def frogJump(self, height):
        # Handle empty input
        if not height:
            return 0

        # Fetch size of the input
        n = len(height)

        # Create dp array where dp[i] = min energy to reach i
        dp = [float('inf')] * n

        # Base case: cost to stand on first stone is zero
        dp[0] = 0

        # Iterate over stones from index 1 to n-1
        for ind in range(1, n):
            # Compute cost for a jump from ind-1
            jump_one = dp[ind - 1] + abs(height[ind] - height[ind - 1])

            # Initialize jump_two with large value
            jump_two = float('inf')

            # If possible, compute cost for a jump from ind-2
            if ind > 1:
                jump_two = dp[ind - 2] + abs(height[ind] - height[ind - 2])

            # Take the minimum of the two options
            dp[ind] = min(jump_one, jump_two)

        # Return min energy to reach last stone
        return dp[-1]


if __name__ == "__main__":
    # Define the heights array
    height = [30, 10, 60, 10, 60, 50]

    # Create Solution instance
    sol = Solution()

    # Compute and print the minimum energy
    print(sol.frogJump(height))  # Expected: 40
