# 풀이
- Difficulty:  Medium
- Topic:  Graphs
- Elapsed Time:  30m
- Status:  O
- Memo: 전혀 어려운 문제가 아닌데 BFS 의 특성을 생각못하고 조건을 넣었다가 시간이 오래 걸렸다.

## 내 풀이
```py
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        EMPTY = 2147483647  # 빈공간
        height = len(rooms)
        width = len(rooms[0])
        dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오 아 왼 위 방향으로 회전

        q = deque()
        for h in range(height):
            for w in range(width):
                if rooms[h][w] == 0:  # gate
                    q.append((h, w))
        if not q:
            return rooms

        while q:
            h, w = q.popleft()
            for dy, dx in dxdy:
                ny = dy + h
                nx = dx + w
                if (
                    0 <= ny
                    and ny < height
                    and 0 <= nx
                    and nx < width
                    and rooms[ny][nx] == EMPTY
                ):
                    rooms[ny][nx] = rooms[h][w] + 1
                    q.append((ny, nx))
        return rooms
```

## 다른 풀이
### Approach 1: (Breadth-first Search) [Accepted]
내 코드랑 비슷함
```py
from collections import deque
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return
        
        EMPTY = 2147483647
        GATE = 0
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        m, n = len(rooms), len(rooms[0])
        q = deque()

        # 모든 게이트를 큐에 추가
        for row in range(m):
            for col in range(n):
                if rooms[row][col] == GATE:
                    q.append((row, col))

        # BFS 실행
        while q:
            row, col = q.popleft()
            for dr, dc in DIRECTIONS:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and rooms[r][c] == EMPTY:
                    rooms[r][c] = rooms[row][col] + 1
                    q.append((r, c))

```