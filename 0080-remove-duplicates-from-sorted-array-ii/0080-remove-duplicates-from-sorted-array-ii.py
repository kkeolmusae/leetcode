class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        count = 1
        n = len(nums)

        while idx < n:
            if nums[idx] == nums[idx - 1]:
                count += 1

                if count > 2:
                    del nums[idx]
                    idx -= 1
                    n -= 1
            else:
                count = 1
            idx += 1
        return len(nums)