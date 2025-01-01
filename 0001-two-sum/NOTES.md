# 풀이
- Difficulty:  Easy
- Topic:  Hashmap
- Elapsed Time:  3m
- Status:  O (2 times)
- Memo:  지난번엔 O(n^2) 으로 풀었는데 이번에는 O(n) 으로 해결함

## 내 풀이
```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for idx in range(len(nums)):
            num = nums[idx]
            if target - num in hash_map:
                return [hash_map[target - num], idx]
            hash_map[num] = idx
        return []
```

## 다른 풀이
### Approach 1: Brute Force
```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        return []
```

### Approach 2: Two-pass Hash Table
```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        return []
```

### Approach 3: One-pass Hash Table
```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
```