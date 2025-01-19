​# 풀이
- Difficulty:  Easy
- Topic:  Heap / Priority Queue
- Elapsed Time:  3m
- Status:  O (2 times)
- Memo:  안어려웠음

## 내 풀이
```py
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = []
        for s in stones:
            heapq.heappush(q, -s)

        while len(q) > 1:
            a = -heapq.heappop(q)
            b = -heapq.heappop(q)

            if a > b:
                heapq.heappush(q, -(a - b))
            elif a < b:
                heapq.heappush(q, -(b - a))

        return 0 if not len(q) else -q[0]
```

## 다른 풀이
### Approach 1: Array-Based Simulation
그냥 비효율적인 방법
```py
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        def remove_largest():
            index_of_largest = stones.index(max(stones))
            return stones.pop(index_of_largest)

        while len(stones) > 1:
            stone_1 = remove_largest()
            stone_2 = remove_largest()
            if stone_1 != stone_2:
                stones.append(stone_1 - stone_2)

        return stones[0] if stones else 0
```

### Approach 2: Sorted Array-Based Simulation
정렬한 다음에 insort 써서 적절한 위치에 값 넣는 방식
```py
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            stone_1 = stones.pop()
            stone_2 = stones.pop()
            if stone_1 != stone_2:
                # insort: 정렬된 시퀀스 a에 x값을 삽입
                bisect.insort(stones, stone_1 - stone_2)
        return stones[0] if stones else 0
```

### Approach 3: Heap-Based Simulation
내 코드랑 비슷
```py
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            if stone_1 != stone_2:
                heapq.heappush(stones, stone_1 - stone_2)

        return -heapq.heappop(stones) if stones else 0
```

### Approach 4: Bucket Sort
```py
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # 버킷 배열 생성
        # 돌의 최대 무게를 기준으로 크기를 정함
        max_weight = max(stones)
        buckets = [0] * (max_weight + 1)

        # 버킷 정렬
        # 각 무게에 해당하는 돌의 개수를 버킷에 저장
        for weight in stones:
            buckets[weight] += 1

        # 무게를 스캔하며 처리
        biggest_weight = 0  # 가장 큰 돌의 무게를 저장
        current_weight = max_weight  # 현재 확인 중인 무게

        while current_weight > 0:
            if buckets[current_weight] == 0:
                # 현재 무게에 해당하는 돌이 없으면 무게를 하나 줄임
                current_weight -= 1
            elif biggest_weight == 0:
                # 가장 큰 돌이 비어있을 경우
                # 현재 무게의 돌 개수를 2로 나눈 나머지를 구함
                buckets[current_weight] %= 2
                if buckets[current_weight] == 1:
                    # 나머지가 1이라면 가장 큰 돌로 설정
                    biggest_weight = current_weight
                # 무게를 하나 줄임
                current_weight -= 1
            else:
                # 가장 큰 돌과 현재 돌을 충돌시킴
                buckets[current_weight] -= 1
                if biggest_weight - current_weight <= current_weight:
                    # 충돌 결과가 현재 무게 이하라면 해당 무게에 돌 추가
                    buckets[biggest_weight - current_weight] += 1
                    # 가장 큰 돌이 없어짐
                    biggest_weight = 0
                else:
                    # 충돌 결과가 현재 무게를 초과한다면 가장 큰 돌 무게 갱신
                    biggest_weight -= current_weight

        # 마지막으로 남은 돌의 무게를 반환
        return biggest_weight

```