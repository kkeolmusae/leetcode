from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        zero_idx = -1
        result = 0

        for idx in range(len(nums)):

            num = nums[idx]
            if num != 1:
                if zero_idx >= 0:  # 0을 여러번 만나는 경우
                    left = zero_idx + 1
                zero_idx = idx
            right += 1

            result = max(result, (right - left) - 1)

        return result