class Solution:
    def robs(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        if n < 3:
            return max(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[n - 1]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        # 첫 번째 집을 털고 마지막 집을 털지 않는 경우와,
        # 첫 번째 집을 털지 않고 마지막 집을 털 수 있는 경우 중 최대 금액 선택
        # 외냐하면 첫번째집이랑 마지막 집이 이어져있다는 조건이 있기 떄문
        return max(self.robs(nums[1:]), self.robs(list(reversed(nums))[1:]))