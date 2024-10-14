class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        dp[0] = 0
        dp[1] = 0
        for idx in range(2, len(cost) + 1):
            # cost[idx - 1] + dp[idx - 1]:  한 단계 전까지의 최소 비용
            # cost[idx - 2] + dp[idx - 2]:  두 단계 전까지의 최소 비용
            dp[idx] = min(cost[idx - 1] + dp[idx - 1], cost[idx - 2] + dp[idx - 2])

        return dp[-1]  # 최소값 리턴