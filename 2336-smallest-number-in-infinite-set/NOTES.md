# 풀이
- LeetCode 75, Medium
- Heap / Priority Queue
- Time: 5m
- 이렇게 푸는게 맞나 싶고... 이게 Medium이 맞나 싶고... 좀 별로였던 문제

## 내 풀이
그냥 문제 그대로 미리 1000까지 넣어놓고 pop하는 경우랑 add하는 경우에 대해서 작성함
```py
class SmallestInfiniteSet:

    def __init__(self):
        self.is_present = set(list(range(1, 1001)))  # 1~1000까지 set이랑 q에 넣어둠
        self.added_integers = list(range(1, 1001))

    def popSmallest(self) -> int:
        if len(self.added_integers):  # 값이 있으면
            num = heapq.heappop(self.added_integers)
            self.is_present.remove(num)  # pop하고 set에서 삭제
            return num

    def addBack(self, num: int) -> None:
        if not num in self.is_present:  # 값이 없는거면
            self.is_present.add(num)  # set에 넣고
            heapq.heappush(self.added_integers, num)  # q에도 넣고

```

## 다른 풀이
### Approach 1: Hashset + Heap
Editorial에 이렇게 나와있던데... 흠 
```py
import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.is_present = set()  # 현재 집합에 있는 정수들을 추적하는 집합
        self.added_integers = []  # 추가된 정수들을 저장하는 최소 힙(min-heap)
        self.current_integer = 1  # 현재 집합에서 사용할 가장 작은 정수

    def popSmallest(self) -> int:
        # 만약 최소 힙에 정수가 있다면, 그 중에서 가장 작은 정수를 팝(pop)하고 반환
        if len(self.added_integers):
            answer = heapq.heappop(self.added_integers)  # 최소 힙에서 가장 작은 값 꺼내기
            self.is_present.remove(answer)  # 꺼낸 값을 집합에서 제거
        # 그렇지 않으면, 현재 집합에서 사용할 가장 작은 정수를 반환하고, 다음 정수로 증가
        else:
            answer = self.current_integer  # 현재 가장 작은 정수를 답으로 설정
            self.current_integer += 1  # 다음에 사용할 정수를 1 증가
        return answer

    def addBack(self, num: int) -> None:
        # 현재 정수보다 크거나 같은 숫자이거나 이미 집합에 존재하는 숫자는 무시
        if self.current_integer <= num or num in self.is_present:
            return
        # 그렇지 않으면, 그 정수를 최소 힙에 추가하고 집합에도 추가
        heapq.heappush(self.added_integers, num)  # 최소 힙에 정수 추가
        self.is_present.add(num)  # 집합에 정수 추가

```

### Approach 2: Sorted Set
흠..
```py
from sortedcontainers import SortedSet

class SmallestInfiniteSet:
    def __init__(self):
        self.added_integers = SortedSet()  # 정렬된 집합으로 추가된 정수들을 관리
        self.current_integer = 1  # 현재 집합에서 사용할 가장 작은 정수

    def popSmallest(self) -> int:
        # 만약 정렬된 집합에 정수가 있다면, 그 중 가장 작은 정수를 꺼내어 반환
        if len(self.added_integers):
            answer = self.added_integers[0]  # 집합의 첫 번째 원소가 가장 작은 정수
            self.added_integers.discard(answer)  # 그 정수를 집합에서 제거
        # 그렇지 않으면, 현재 집합에서 사용할 가장 작은 정수를 반환하고, 다음 정수로 증가
        else:
            answer = self.current_integer  # 현재 가장 작은 정수를 반환
            self.current_integer += 1  # 다음에 사용할 정수를 1 증가
        return answer

    def addBack(self, num: int) -> None:
        # 현재 정수보다 크거나 같거나, 이미 정렬된 집합에 있는 숫자는 무시
        if self.current_integer <= num or num in self.added_integers:
            return
        # 그렇지 않으면, 그 정수를 정렬된 집합에 추가
        self.added_integers.add(num)  # 정수를 정렬된 집합에 추가
```