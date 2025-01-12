# 풀이
- Difficulty:  Medium
- Topic:  Backtracking
- Elapsed Time:  2m
- Status:  O
- Memo: 파이썬이라서 이렇게 풀었다....

## 내 풀이
```py
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums, len(nums)))
```

## 다른 풀이
### Approach: Backtracking
```py
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        ans = []
        backtrack([])
        return ans
```