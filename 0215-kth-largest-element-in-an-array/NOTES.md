​# 풀이
- LeetCode 75, Medium
- Heap / Priority Queue
- Time: 0m
- 예전에 풀었던거라 주석만 추가함

## 내 풀이
```py
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for num in nums:
            heapq.heappush(q, num)  # 일단 넣고

            if len(q) > k:  # k개 보다 크면 pop해서 k개 까지만 넣어두면
                heapq.heappop(q)
        return q[0]  # q[0]에 있는 값이 k번째로 큰 값
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