# 풀이
- Difficulty:  Easy
- Topic:  Array / String
- Elapsed Time:  2m
- Status:  O (1 times)
- Memo: 쉬운 문제다.

## 내 풀이
문제를 잘못 이해하고 풀어서 시간효율성이 다른 풀이에 비해 별로다. 문제를 잘 읽어보는 습관을 기르자.
```py
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        n = len(nums)

        for num in nums:  # 삭제하고자 하는 숫자 몇개인지 
            if val == num:
                cnt += 1

        for _ in range(cnt):  # 숫자 개수만큼 remove 
            nums.remove(val)

        return n - cnt
```

## 다른 풀이
### Approach 1: Two Pointers
```py
# Python3
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
```

### Approach 2: Two Pointers - when elements to remove are rare
```py
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n
```
