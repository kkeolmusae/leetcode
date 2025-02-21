class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)  # dp 초기화
        dp[0] = 0

        coins.sort()

        for c in coins:
            for a in range(c, amount + 1):
                dp[a] = min(dp[a], dp[a - c] + 1)

        return -1 if dp[amount] == math.inf else dp[amount]