class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for idx in range(len(nums) - 1):
            if nums[idx] > nums[idx + 1]:
                return idx

        return len(nums) - 1
