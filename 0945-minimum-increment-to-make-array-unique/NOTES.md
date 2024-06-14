### NOTES 
처음에 for문 여러개로 풀었다가 시간초과 발생해서 heapq로 풀었다.

for문 하나로 푸는 방법은
```python
from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        min_increments = 0

        nums.sort()

        for i in range(1, len(nums)):
            # Ensure each element is greater than its previous
            if nums[i] <= nums[i - 1]:
                # Add the required increment to minIncrements
                increment = nums[i - 1] + 1 - nums[i]
                min_increments += increment

                # Set the element to be greater than its previous
                nums[i] = nums[i - 1] + 1

        return min_increments
```

이렇다.