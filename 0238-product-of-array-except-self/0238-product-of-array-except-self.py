from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_count = 0
        
        for num in nums:
            if num == 0:
                zero_count += 1
                if zero_count > 1:
                    total = 0
            else:
                total *= num
        
        result = []
        
        if zero_count > 1:
            return [0] * len(nums)
        else:
            for num in nums:
                if num == 0:
                    result.append(total)
                elif zero_count > 0:
                    result.append(0)
                else:
                    result.append(total // num)
            
        return result