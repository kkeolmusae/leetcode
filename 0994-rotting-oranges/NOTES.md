# 풀이
- Difficulty:  Medium
- Topic:  Graphs
- Elapsed Time:  10m
- Status:  O (2 times)
- Memo:  지난번에 풀어봤던 문제라 금방 품

## 내 풀이
지난번에는 checked 라는 변수를 써서 체크한 오렌지를 기록했는데, 이번에는 안쓰고 해결함
```py
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오 아 왼 위 방향으로 회전

        q = deque()
        total = 0
        for h in range(height):
            for w in range(width):
                if grid[h][w] == 2:  # 썩은 오렌지
                    q.append((h, w, 0))
                elif grid[h][w] == 1:  # 멀쩡한 오렌지
                    total += 1

        result = 0
        while q:
            h, w, t = q.popleft()
            for dy, dx in dxdy:
                ny = dy + h
                nx = dx + w
                if 0 <= ny < height and 0 <= nx < width and grid[ny][nx] == 1:
                    grid[ny][nx] = 2
                    q.append((ny, nx, t + 1))
                    result = max(result, t + 1)
                    total -= 1

        return result if total == 0 else -1
```

## 다른 풀이
### Approach 1: Breadth-First Search (BFS)
내 코드랑 time 을 처리하는 부분을 제외하고 거의 동일함
```py
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        # Step 1). 초기 썩은 오렌지를 큐에 추가하고, 신선한 오렌지 개수 계산
        fresh_oranges = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))  # 썩은 오렌지 위치 저장
                elif grid[r][c] == 1:
                    fresh_oranges += 1  # 신선한 오렌지 개수 증가

        # 타임스탬프를 위한 마커로 (-1, -1) 추가
        queue.append((-1, -1))

        # Step 2). BFS를 통해 썩는 과정을 시작
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상, 우, 하, 좌 방향
        while queue:
            row, col = queue.popleft()  # 큐에서 현재 위치 꺼냄
            if row == -1:
                # 한 라운드의 처리가 끝난 경우
                minutes_elapsed += 1
                if queue:  # 큐가 비어 있지 않다면 다음 라운드 시작
                    queue.append((-1, -1))  # 타임스탬프 마커 추가
            else:
                # 썩은 오렌지의 위치에서 주변 오렌지를 확인
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            # 신선한 오렌지를 썩게 만듦
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1  # 신선한 오렌지 개수 감소
                            # 썩은 오렌지를 큐에 추가하여 다음에 처리
                            queue.append((neighbor_row, neighbor_col))

        # 모든 신선한 오렌지가 썩었다면 경과된 시간을 반환, 그렇지 않다면 -1 반환
        return minutes_elapsed if fresh_oranges == 0 else -1

```

### Approach 2: In-place BFS
Apporach 1 에 비해 시간 복잡도가 증가한 코드... 접근법이 조금 특이하다고 생각했다.
```py
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # 썩은 오렌지가 퍼지는 과정을 실행, 썩은 오렌지를 타임스탬프로 표시
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상, 우, 하, 좌 방향

        # 썩은 오렌지가 주변의 신선한 오렌지를 썩게 만드는 과정
        def runRottingProcess(timestamp):
            # 썩는 과정을 계속할지 여부를 나타내는 플래그
            to_be_continued = False
            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == timestamp:
                        # 현재 썩은 오렌지의 위치에서 인접한 오렌지를 확인
                        for d in directions:
                            n_row, n_col = row + d[0], col + d[1]
                            if ROWS > n_row >= 0 and COLS > n_col >= 0:
                                if grid[n_row][n_col] == 1:
                                    # 신선한 오렌지가 썩게 됨
                                    grid[n_row][n_col] = timestamp + 1
                                    to_be_continued = True
            return to_be_continued

        # 썩는 과정 시작, 처음 타임스탬프는 2로 설정
        timestamp = 2
        while runRottingProcess(timestamp):
            timestamp += 1
        
        # 썩는 과정이 끝난 후, 신선한 오렌지가 남아 있는지 확인
        for row in grid:
            for cell in row:
                if cell == 1:  # 신선한 오렌지가 남아 있으면 -1 반환
                    return -1

        # 모든 신선한 오렌지가 썩었을 경우 경과된 시간을 반환
        return timestamp - 2

```

### Approach 3:
```py
```