class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float("inf")  # dp[amount]의 최소값을 구해야하기 때문에 inf로 초기 세팅
        dp = [INF] * (amount + 1)
        dp[0] = 0

        coins.sort()  # 오름차순으로 정렬

        for coin in coins:
            for a in range(coin, amount + 1):  # dp[amount] 까지 해야해서 +1 해줌
                # dp[a] 를 만드는데 필요한 최소 코인 = min(dp[a], dp[a-coin] + 1)
                dp[a] = min(dp[a], dp[a - coin] + 1)

        return dp[amount] if dp[amount] != INF else -1