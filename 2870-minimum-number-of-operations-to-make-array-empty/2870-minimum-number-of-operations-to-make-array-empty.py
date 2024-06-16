from typing import List
from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums_count = Counter(nums)
        
        result = 0
        for num in nums_count:
            count = nums_count[num]
            if count == 1:
                return -1

            result += count // 3
            if count % 3 != 0: # 3으로 딱 떨어지는게 아니면 1 더해주기
                result += 1
            
        return result