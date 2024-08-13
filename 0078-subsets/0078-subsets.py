from itertools import combinations
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        for i in range(n + 1):
            l = list(combinations(nums, i))
            for li in l:
                result.append(list(li))

        return result