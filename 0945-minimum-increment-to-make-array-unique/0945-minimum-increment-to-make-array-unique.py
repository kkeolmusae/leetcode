import heapq
from typing import List
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        arr = []
        heapq.heapify(nums)
        num = heapq.heappop(nums)
        arr.append(num)
        
        result = 0
        while nums:
            num = heapq.heappop(nums)
                
            if arr[-1] >= num:
                arr.append(arr[-1] + 1)
                result += arr[-1] - num
            else:
                arr.append(num)
        
        return result