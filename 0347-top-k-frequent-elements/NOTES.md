## 다른 풀이
### 단순하게 구현
내가 짠 코드랑 비슷한데 파이썬 내부 함수를 사용해서 더 단순하고 간결하게 구현함. 시간복잡도도 조금 더 나음 (내껀 NlogN, 이거는 Nlogk)
```py
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. Build hash map: character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. Build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get) 
```