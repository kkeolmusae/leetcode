class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        if n < 3:
            return max(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[n - 1]
