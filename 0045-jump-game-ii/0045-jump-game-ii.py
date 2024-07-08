import math
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)

        if l == 1:
            return 0
        dp = [math.inf] * l
        for i in range(l):
            for j in range(i + 1, min(i + 1 + nums[i], l)):
                if dp[i] == math.inf:
                    dp[j] = 1
                else:
                    dp[j] = min(dp[i] + 1, dp[j])
        return dp[l - 1]