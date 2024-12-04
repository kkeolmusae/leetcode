​# 풀이
- Difficulty: Medium
- Topic:  Heap / Priority Queue
- Elapsed Time:  2m
- Status:  O (3 times)
- Time: 2m
- Memo: 세번째 푸는거라 어려움 없이 풀었음

## 내 풀이
```py
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []

        for num in nums:
            heapq.heappush(q, num)

            if len(q) > k:
                heapq.heappop(q)

        return heapq.heappop(q)
```

## 다른 풀이
### Approach 1: Sort
걍 정렬...
```py
class Solution:
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        return nums[k - 1]
```

### Approach 2: Min-Heap
```py
class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]
```

### Approach 3: Quickselect
퀵정렬? 비슷하게 푸는 방법. 
```py
import random

class Solution:
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            pivot = random.choice(nums)  # 피벗을 랜덤으로 선택
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:  # 피벗보다 큰 값은 left 리스트에 추가
                    left.append(num)
                elif num < pivot:  # 피벗보다 작은 값은 right 리스트에 추가
                    right.append(num)
                else:  # 피벗과 같은 값은 mid 리스트에 추가
                    mid.append(num)
            
            if k <= len(left):  # k번째 큰 값이 left 리스트에 있는 경우
                return quick_select(left, k)
            
            if len(left) + len(mid) < k:  # k번째 큰 값이 right 리스트에 있는 경우
                return quick_select(right, k - len(left) - len(mid))
            
            return pivot  # 피벗이 k번째 큰 값인 경우
        
        return quick_select(nums, k)  # k번째 큰 값을 반환

```