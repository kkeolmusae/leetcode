# 풀이
중간값을 찾는 문제

## 내 풀이​
heap 을 두개 써서 품.
```py
import heapq


class MedianFinder:

    def __init__(self):
        self.hi = []  # 큰 숫자들을 min heap으로 넣기
        self.lo = []  # 작은 숫자들을 max heap으로 넣기

    def addNum(self, num: int) -> None:
        heapq.heappush(self.hi, num)  # 일단 hi에 넣고

        # hi에서 제일 작은 값을 lo로 옮김
        heapq.heappush(self.lo, -heapq.heappop(self.hi))

        if len(self.hi) < len(self.lo):
            # lo 에서 가장 큰 숫자를 hi로 옮기자
            heapq.heappush(self.hi, -heapq.heappop(self.lo))

    def findMedian(self) -> float:

        if len(self.lo) == len(self.hi):
            return (-self.lo[0] + self.hi[0]) / 2
        return self.hi[0]


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
print(obj.addNum(-1))
print(obj.findMedian())
print(obj.addNum(-2))
print(obj.findMedian())
print(obj.addNum(-3))
print(obj.findMedian())
print(obj.addNum(-4))
print(obj.findMedian())
print(obj.addNum(-5))
print(obj.findMedian())
```

## 다른 풀이
### Approach 1: Simple Sorting
정말 단순히 정렬해서 중간값을 찾는 방법
```py
class MedianFinder:
    def __init__(self):
        # List to store numbers
        self.store = []

    # Adds a number into the data structure.
    def addNum(self, num: int) -> None:
        self.store.append(num)

    # Returns the median of the current data stream.
    def findMedian(self) -> float:
        # Sort the list
        self.store.sort()
        n = len(self.store)
        
        # If the list has an odd length, return the middle element
        if n % 2 == 1:
            return self.store[n // 2]
        # If the list has an even length, return the average of the two middle elements
        else:
            return (self.store[n // 2 - 1] + self.store[n // 2]) / 2.0

```

### Approach 2: Insertion Sort
숫자를 추가할 때, 이미 정렬된 위치에 이분 탐색을 통해 숫자를 삽입하는 방식으로 데이터를 관리
```py
import bisect

class MedianFinder:
    def __init__(self):
        # List to store numbers
        self.store = []

    # Adds a number into the data structure
    def addNum(self, num: int) -> None:
        # Insert the number at the correct position to keep the list sorted
        bisect.insort(self.store, num)

    # Returns the median of the current data stream
    def findMedian(self) -> float:
        n = len(self.store)
        # If the length is odd, return the middle element
        if n % 2 == 1:
            return self.store[n // 2]
        # If the length is even, return the average of the two middle elements
        else:
            return (self.store[n // 2 - 1] + self.store[n // 2]) / 2.0

```