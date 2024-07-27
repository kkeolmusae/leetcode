from typing import List


class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        min_num = 1000001
        max_num = -1

        min_idx = 0
        max_idx = 0

        for idx in range(n):
            if min_num > nums[idx]:
                min_idx = idx
                min_num = nums[idx]

            if nums[idx] >= max_num:
                max_idx = idx
                max_num = nums[idx]

        if min_idx > max_idx:
            return min_idx + (n - 1) - (max_idx + 1)
        else:
            return min_idx + (n - 1) - max_idx