class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float("inf")  # dp[amount]의 최소값을 구해야하기 때문에 inf로 초기 세팅
        dp = [INF] * (amount + 1)
        dp[0] = 0

        coins.sort()
        for c in coins:
            for a in range(c, amount + 1):
                dp[a] = min(dp[a], dp[a - c] + 1)
        return dp[amount] if dp[amount] != INF else -1