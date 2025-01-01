# 풀이
- Difficulty:  Medium
- Topic:  Arrays & Hashing
- Elapsed Time:  2m
- Status:  O (2 times)
- Memo:

## 내 풀이
```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = defaultdict(int)

        for n in nums:
            dict[n] += 1

        q = []
        for key, val in dict.items():
            # 빈도가 많은게 우선순위가 높게 하기 위해서 - 붙임
            heapq.heappush(q, (-val, key))

        result = []
        while k:
            val, key = heapq.heappop(q)
            result.append(key)
            k -= 1
        return result
```

## 다른 풀이
### Approach 1: Heap
- 파이썬 내부 함수를 사용해서 더 단순하고 간결하게 구현함
- 시간복잡도도 조금 더 나음 (내껀 NlogN, 이거는 Nlogk)
```py
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        if k == len(nums):
            return nums

        count = Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get) 
```