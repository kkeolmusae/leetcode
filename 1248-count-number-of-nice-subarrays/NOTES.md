### Notes
처음에 이렇게 풀었는데 Time Limit Exceeded 뜸. 나중에 다시 풀어보자. 접근방식에 대해서만 100% 이해하면 금방 풀 수 있는 문제임 
```python
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [num % 2 for num in nums]
        
        total_odd_count = sum(nums)
        nums_size = len(nums)
    
        if total_odd_count < k:
            return 0
        
        
        result = 0
        size = k
        while size <= nums_size:
            total = sum(nums[0: size])
            if total == k:
                result += 1
            for idx in range(1, nums_size - size + 1):
                total += nums[idx + size - 1]
                total -= nums[idx - 1]
                if total == k:
                    result += 1
            size += 1      
        return result

# nums = [1,1,2,1,1]
# k = 3
#Output: 2

# nums = [2,4,6]
# k = 1
# #Output: 0

# nums = [2,2,2,1,2,2,1,2,2,2]
# k = 2
# #Output: 16

nums = [1,1,2,1,1,1,1,2,1,11,1,2,1,11,1,2,1,11,1,2,1,11,1,2,1,1]
k = 3
# #Output: 32
```

