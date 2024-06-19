from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = []
        for idx in range(len(nums)):
            result.append(nums[nums[idx]])
        return result