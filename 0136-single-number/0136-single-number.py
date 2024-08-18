from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        idx = 0
        while idx < len(nums) - 1:
            if nums[idx] != nums[idx + 1]:
                return nums[idx]

            idx += 2
        return nums[idx]