# 풀이
배열에서 고유의 숫자를 리턴하는 문제. neetcode에서 Bit Manipulation 유형의 문제였는데 어떻게 접근해야할지 몰라서 일단 내 생각대로 풀어봄

## 내 풀이​
단순히 정렬하고, 똑같은 숫자 있는지 체크하는 방법으로 해결함
```py
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        idx = 0
        while idx < len(nums) - 1:
            if nums[idx] != nums[idx + 1]:
                return nums[idx]

            idx += 2
        return nums[idx]
```

## 다른 풀이
### Approach 4: Bit Manipulation
- a ^ 0 = a
- a ^ a = 0
- a ^ a ^ b = (a ^ a) ^ b = 0 ^ b = b 의 방식으로 풀림
```py
class Solution(object):
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
```