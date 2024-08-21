from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        cnt = 0

        while i < j:
            left = nums[i]
            right = nums[j]
            if left + right == k:
                i += 1
                j -= 1
                cnt += 1
            elif left + right > k:  # 두 수의 합이 k 보다 크면 큰 수를 작게
                j -= 1
            else:  # 두 수의 합이 k 보다 작으면 작은수를 크게
                i += 1
        return cnt