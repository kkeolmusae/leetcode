# 풀이
- Difficulty:  Medium
- Topic:  Graphs
- Elapsed Time:  10m
- Status:  O 
- Memo: 단순 Graph 문제라서 쉽게 풀었다.

## 내 풀이
```py
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        answer = 0

        width = len(grid[0])
        heigth = len(grid)

        dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오 아 왼 위 방향으로 회전

        def bfs(h, w):
            q = deque()
            q.append((h, w))
            grid[h][w] = 0
            count = 1

            while q:
                h, w = q.popleft()
                for dy, dx in dxdy:
                    ny = h + dy
                    nx = w + dx
                    if (
                        0 <= ny
                        and ny < heigth
                        and 0 <= nx
                        and nx < width
                        and grid[ny][nx] == 1
                    ):
                        grid[ny][nx] = 0
                        q.append((ny, nx))
                        count += 1
            return count

        for h in range(heigth):
            for w in range(width):
                if grid[h][w] == 1:
                    result = bfs(h, w)
                    answer = max(answer, result)
        return answer
```

## 다른 풀이
### Approach #1: Depth-First Search (Recursive) [Accepted]
dfs 
```py
class Solution(object):
    def maxAreaOfIsland(self, grid):
        seen = set()  # 이미 방문한 셀을 추적하기 위한 집합

        def area(r, c):
            # 유효하지 않은 셀 조건 확인:
            # 1. 그리드 범위를 벗어남
            # 2. 이미 방문한 셀
            # 3. 물(0)인 경우
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            
            seen.add((r, c))  # 현재 셀을 방문했다고 표시
            
            # 현재 셀(1)과 인접한 네 방향의 셀들의 면적을 재귀적으로 합산
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))

        # 그리드의 모든 셀에 대해 area 함수를 호출하고, 최대값을 반환
        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))

```

### Approach #2: Depth-First Search (Iterative) [Accepted]
Approach 1 은 재귀함수로 해결했다면 2는 Iterative으로 해결했다.
```py
class Solution(object):
    def maxAreaOfIsland(self, grid):
        seen = set()  # 이미 방문한 셀을 추적하기 위한 집합
        ans = 0  # 최대 섬 면적을 저장할 변수
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                # 현재 셀이 땅(1)이고 아직 방문하지 않았다면
                if val and (r0, c0) not in seen:
                    shape = 0  # 현재 섬의 면적
                    stack = [(r0, c0)]  # DFS를 위한 스택
                    seen.add((r0, c0))  # 현재 셀을 방문했다고 표시
                    while stack:
                        r, c = stack.pop()  # 스택에서 셀 좌표를 꺼냄
                        shape += 1  # 섬의 면적 증가
                        # 상하좌우 네 방향의 인접 셀 확인
                        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            # 인접 셀이 유효하고, 땅이며, 아직 방문하지 않았다면
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                    and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc))  # 스택에 추가
                                seen.add((nr, nc))  # 방문했다고 표시
                    ans = max(ans, shape)  # 최대 섬 면적 갱신
        return ans  # 최대 섬 면적 반환
```