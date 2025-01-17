​# 풀이
- Difficulty:  Easy
- Topic:  Heap / Priority Queue
- Elapsed Time:  5m
- Status:  O (2 times)
- Memo:  난이도가 Easy라서 금방 풀었다. 

## 내 풀이
```py
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.q = []
        self.k = k

        for num in nums:
            heapq.heappush(self.q, num)
            if len(self.q) > k:  # k개 유지
                heapq.heappop(self.q)

    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)
        if len(self.q) > self.k:
            heapq.heappop(self.q)
        return self.q[0]
```

## 다른 풀이
### Approach 1: Maintain Sorted List
정렬하고 k 위치에 놓는 방법으로 풀렸다.
```py
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = nums
        # 주어진 배열을 정렬
        self.stream.sort()

    def add(self, val: int) -> int:
        # 새로운 값이 들어갈 위치를 이진 탐색으로 찾음
        index = self.getIndex(val)
        # 값을 올바른 위치에 삽입
        self.stream.insert(index, val)
        # k번째로 큰 값을 반환
        return self.stream[-self.k]

    def getIndex(self, val: int) -> int:
        # 이진 탐색으로 삽입 위치를 찾음
        left, right = 0, len(self.stream) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_element = self.stream[mid]
            # 현재 값이 찾으려는 값과 같다면 해당 인덱스를 반환
            if mid_element == val:
                return mid
            # 중간값이 찾으려는 값보다 크다면 왼쪽 구간 탐색
            elif mid_element > val:
                right = mid - 1
            # 중간값이 찾으려는 값보다 작다면 오른쪽 구간 탐색
            else:
                left = mid + 1
        # 삽입 위치 반환 (left 값이 최종 위치)
        return left

```

### Approach 2: Heap
내 코드랑 얼추 비슷하다
```py
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k or self.min_heap[0] < val:
            heapq.heappush(self.min_heap, val)
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)
        return self.min_heap[0]
```