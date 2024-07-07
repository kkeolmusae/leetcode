from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_idx = len(nums) - 1
        
        for idx in range(len(nums) - 1, -1, -1):
            if idx + nums[idx] >= last_idx:
                last_idx = idx
        return last_idx == 0