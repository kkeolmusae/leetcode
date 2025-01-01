# 풀이
- Difficulty:  Easy
- Topic:  Arrays & Hashing
- Elapsed Time:  1m
- Status:  O (2 times)
- Memo:  쉬운 문제

## 내 풀이
```py
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}

        for n in nums:
            if n in dict:
                return True
            dict[n] = False
        return False
```

## 다른 풀이
### Approach 1: One Line
```py
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return True if len(set(nums)) < len(nums) else False
```