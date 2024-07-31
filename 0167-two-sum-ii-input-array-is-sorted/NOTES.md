# 풀이
처음에 풀었다가 해설보고 다시 품.
## 내 풀이
1. 일단 무조건 사다리를 쓰고, (채워 넣어야하는 벽돌 > 이전에 사용한 사다리) 이면 사다리를 벽돌로 대체하는 방법으로 풀림
2. 사용중인 사다리는 heapq에 넣어서 가장 작은 범위를 해결한 사다리가 앞에 오게 함
- 시간 복잡도: O(NlogN) or O(NlogL)  (L: 사다리 개수, N: 건물 개수)

```py
import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        q = []  # 사용한 사다리(얼마의 길이에 썼는지)
        n = len(heights)

        for idx in range(n - 1):
            curr = heights[idx]
            next = heights[idx + 1]

            # 두 건물의 차이
            diff = next - curr

            if diff <= 0:
                continue

            # 사다리 있으면 무조건 사다리 부터 씀
            if ladders:
                ladders -= 1
                heapq.heappush(q, diff)
                continue

            # 여분 사다리 없는 경우
            # 사용했던 사다리중에 제일 짧은게 diff보다 작으면 벽돌로 대체
            if q and q[0] < diff:
                prev_ladders = heapq.heappop(q)  # 이전에 쓴 사다리 빼고
                bricks -= prev_ladders  # 벽돌로 채워넣고
                heapq.heappush(q, diff)  # 사다리 사용
            else:
                bricks -= diff

            if bricks < 0:
                return idx

        return n - 1  # 끝까지 간 경우
```

## 다른 풀이

### Min Heap
내 풀이의 기반이 된 코드
```py
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_allocations = [] # We'll use heapq to treat this as a min-heap.
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            # If this is actually a "jump down", skip it.
            if climb <= 0:
                continue
            # Otherwise, allocate a ladder for this climb.
            heapq.heappush(ladder_allocations, climb)
            # If we haven't gone over the number of ladders, nothing else to do.
            if len(ladder_allocations) <= ladders:
                continue
            # Otherwise, we will need to take a climb out of ladder_allocations
            bricks -= heapq.heappop(ladder_allocations)
            # If this caused bricks to go negative, we can't get to i + 1
            if bricks < 0:
                return i
        # If we got to here, this means we had enough to cover every climb.
        return len(heights) - 1
```

### Max Heap
min heap은 사다리를 먼저쓰고 나중에 벽돌로 대체하는 방식이었다면, max heap은 벽돌을 먼저 쓰고 사다리로 대체하는 방식으로 구현됨

```py
import heapq
from typing import List

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # Create a max-heap using a min-heap with negative values
        brick_allocations = []
        
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            # If this is a "jump down", skip it.
            if climb <= 0:
                continue
            
            # Allocate bricks or ladders for this climb
            heapq.heappush(brick_allocations, -climb)
            bricks -= climb
            
            # If we've used all the bricks and have no ladders left, we can't go further
            if bricks < 0 and ladders == 0:
                return i
            
            # If we've run out of bricks, replace the largest brick allocation with a ladder
            if bricks < 0:
                bricks += -heapq.heappop(brick_allocations)
                ladders -= 1
        
        # If we reach here, we have enough materials to cover every climb
        return len(heights) - 1
```