class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            # (i-1 에서 올라오는 경우) + (i-2 에서 올라오는 경우)
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]