from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        result = nums[0]
        
        for idx in range(1, len(nums)):
            dp[idx] = max(nums[idx] + dp[idx - 1], nums[idx])
            result = max(dp[idx], result)
        return result