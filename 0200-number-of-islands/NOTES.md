- # 풀이
- Difficulty:  Medium
- Topic:  Graphs
- Elapsed Time:  25m
- Status:  O (2 times)
- Memo: 오랜만에 풀어서 삽질하다가 시간을 많이 썼다.

## 내 풀이
Memory Limit Exceeded 방지를 위해 q에 넣기전에 미리 방문처리를 해야한다.
```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        width = len(grid[0])
        height = len(grid)

        dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오 아 왼 위 방향으로 회전

        def bfs(point):
            y, x = point
            q = deque()
            q.append((y, x))

            while q:
                y, x = q.popleft()

                for dy, dx in dxdy:
                    nx = dx + x
                    ny = dy + y
                    if (
                        0 <= nx
                        and nx < width
                        and 0 <= ny
                        and ny < height
                        and grid[ny][nx] == "1"
                    ):
                        # q에 넣기 전에 미리 방문처리를 해둠으로서 q에 필요한 것만 들어가게함 (Memory Limit Exceeded 방지)
                        grid[ny][nx] = "0"
                        q.append((ny, nx))

        for h in range(height):
            for w in range(width):
                if grid[h][w] == "1":
                    bfs((h, w))
                    answer += 1
        return answer

```

## 다른 풀이
### Approach #1 DFS [Accepted]
재귀함수로 풀이
```py
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        num_islands = 0
        # 격자의 모든 셀을 순회하면서 섬을 찾는다.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 현재 셀이 '1'인 경우 섬이 발견된 것이므로 DFS를 시작한다.
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    num_islands += 1

        return num_islands

    def dfs(self, grid, r, c):
        # DFS 종료 조건:
        # 격자의 범위를 벗어나거나, 현재 셀이 '1'이 아닌 경우
        if (
            r < 0
            or c < 0
            or r >= len(grid)
            or c >= len(grid[0])
            or grid[r][c] != "1"
        ):
            return
        # 현재 셀을 '0'으로 바꿔 방문했음을 표시한다.
        grid[r][c] = "0"

        # 상하좌우로 이동하여 연결된 모든 '1'을 방문 처리한다.
        self.dfs(grid, r - 1, c)  # 위쪽
        self.dfs(grid, r + 1, c)  # 아래쪽
        self.dfs(grid, r, c - 1)  # 왼쪽
        self.dfs(grid, r, c + 1)  # 오른쪽

```

### Approach #2: BFS [Accepted]
내 코드랑 비슷함.
```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        nr = len(grid)  # 격자의 행 수
        nc = len(grid[0])  # 격자의 열 수
        num_islands = 0

        # 격자의 모든 셀을 순회하며 섬을 찾는다.
        for r in range(nr):
            for c in range(nc):
                # 현재 셀이 '1'인 경우 새로운 섬을 발견한 것이므로 BFS를 시작한다.
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"  # 방문 처리
                    neighbors = [(r, c)]  # BFS를 위한 큐 초기화
                    
                    # 큐를 사용해 연결된 모든 '1'을 탐색하며 방문 처리한다.
                    while neighbors:
                        row, col = neighbors.pop(0)
                        # 상하좌우로 이동하며 이웃을 탐색
                        if row - 1 >= 0 and grid[row - 1][col] == "1":
                            neighbors.append((row - 1, col))
                            grid[row - 1][col] = "0"  # 방문 처리
                        if row + 1 < nr and grid[row + 1][col] == "1":
                            neighbors.append((row + 1, col))
                            grid[row + 1][col] = "0"  # 방문 처리
                        if col - 1 >= 0 and grid[row][col - 1] == "1":
                            neighbors.append((row, col - 1))
                            grid[row][col - 1] = "0"  # 방문 처리
                        if col + 1 < nc and grid[row][col + 1] == "1":
                            neighbors.append((row, col + 1))
                            grid[row][col + 1] = "0"  # 방문 처리

        return num_islands

```

### Approach #3: Union Find (aka Disjoint Set) [Accepted]
Union Find로 푼건데 아직 Union Find가 익숙치 않다..
```py
class UnionFind:
    def __init__(self, grid):
        self.count = 0
        m, n = len(grid), len(grid[0])
        self.parent = []
        self.rank = []

        # Union-Find 자료 구조 초기화
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    # '1'인 경우 고유한 parent로 초기화하고 섬의 개수를 증가시킴.
                    self.parent.append(i * n + j)
                    self.count += 1
                else:
                    # '0'인 경우, parent를 -1로 설정.
                    self.parent.append(-1)
                self.rank.append(0)

    # 경로 압축을 이용한 find 함수
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    # union 함수는 두 요소의 루트를 찾고 합칩니다.
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            # rank를 기준으로 루트를 연결합니다.
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            # 두 개의 집합이 합쳐지므로 섬의 개수를 1 줄입니다.
            self.count -= 1

    def getCount(self):
        return self.count


class Solution:
    def numIslands(self, grid):
        # 기본 예외 처리
        if not grid or not grid[0]:
            return 0

        nr = len(grid)
        nc = len(grid[0])
        # Union-Find 구조 초기화
        uf = UnionFind(grid)

        # 모든 셀을 순회하면서 '1'인 셀의 상하좌우를 탐색
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    # 현재 셀을 방문한 것으로 처리
                    grid[r][c] = "0"
                    # 상하좌우의 '1'들과 합집합 처리
                    if r - 1 >= 0 and grid[r - 1][c] == "1":
                        uf.union(r * nc + c, (r - 1) * nc + c)
                    if r + 1 < nr and grid[r + 1][c] == "1":
                        uf.union(r * nc + c, (r + 1) * nc + c)
                    if c - 1 >= 0 and grid[r][c - 1] == "1":
                        uf.union(r * nc + c, r * nc + c - 1)
                    if c + 1 < nc and grid[r][c + 1] == "1":
                        uf.union(r * nc + c, r * nc + c + 1)

        # 최종적으로 남은 집합의 개수(섬의 수)를 반환
        return uf.getCount()

```