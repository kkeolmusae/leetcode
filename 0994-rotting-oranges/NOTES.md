# 풀이
- LeetCode 75, Medium
- Graphs - BFS
- Time: 17m 23s
- 비슷한 유형의 문제를 예전에 백준에서 풀어봤어서 그런지 크게 어렵지 않았음.

## 내 풀이
```py
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0: 빈셀, 1: fresh, 2: rotten

        q = deque()  # 썩은 오렌지 위치 저장
        fresh_cnt = 0  # 신선한 오렌지 개수 저장
        result = 0  # 걸린 시간

        garo = len(grid[0])
        sero = len(grid)

        dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오 아 왼 위 방향으로 회전
        checked = defaultdict(bool)

        for i in range(sero):
            for j in range(garo):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh_cnt += 1

        while q:
            cx, cy, ctime = q.popleft()  # 현재 x,y,time
            result = max(ctime, result)
            if checked[(cx, cy)]:  # 확인한적있는 곳이면 패스
                continue
            checked[(cx, cy)] = True  # 확인 처리

            for dx, dy in dxdy:
                nx = cx + dx
                ny = cy + dy
                if nx >= 0 and nx < sero and ny >= 0 and ny < garo:  # 범위내
                    if grid[nx][ny] == 1:  # 신선한 과일 발견
                        grid[nx][ny] = 2  # 감염처리
                        q.append((nx, ny, ctime + 1))
                        fresh_cnt -= 1

        if fresh_cnt > 0:  # 신선한게 남아있으면
            return -1
        return result

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