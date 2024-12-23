class Solution:
    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[n - 1]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return max(nums)
        return max(self.rob1(nums[1:]), self.rob1(list(reversed(nums))[1:]))