from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        nums.sort()
        
        max_longest_consectuive = 0
        
        prev_num = nums[0]
        cnt = 1
        for idx in range(1, len(nums)):
            if nums[idx] - prev_num == 1:
                cnt += 1
            elif nums[idx] == prev_num:
                continue
            else:
                max_longest_consectuive = max(cnt, max_longest_consectuive)
                cnt = 1
            prev_num = nums[idx]

        max_longest_consectuive = max(cnt, max_longest_consectuive)
        return max_longest_consectuive  