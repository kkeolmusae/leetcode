from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0

        while j < len(nums):
            while i < len(nums) and nums[i] != 0:  # i는 0을 찾아다니고
                i += 1

            while j < len(nums) and nums[j] == 0:  # j는 0 아닌걸 찾아다니고
                j += 1

            if j >= len(nums) or i >= len(nums):
                break

            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return nums