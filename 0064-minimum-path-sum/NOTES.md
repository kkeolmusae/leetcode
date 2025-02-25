# 풀이
- Difficulty:  Medium
- Topic:  Multidimensional DP
- Elapsed Time:  20m
- Status:  O
- Approach:  BFS 로 접근했다가 메모리 초과로 인해서 DP로 변환해서 해결했다.
- Memo:  처음에 BFS 로 풀었다가 메모리 초과 발생해서 DP 로 풀었다. 

## 내 풀이
이동할 수 있는 방향이 아래쪽, 오른쪽 이라는 것을 생각해서 구현했다. 어렵지 않았다.
```py
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])

        for i in range(h):
            for j in range(w):
                if i == 0 and j == 0:
                    continue
                elif i == 0:  # 첫 번째 행 (오른쪽으로만 이동 가능)
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:  # 첫 번째 열 (아래쪽으로만 이동 가능)
                    grid[i][j] += grid[i - 1][j]
                else:  # 두 방향에서 최소값 선택
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]  # 우하단의 값이 최소 경로 합
```

## 다른 풀이
### Approach 1: Brute Force
```py
class Solution:
    def calculate(self, grid: List[List[int]], i: int, j: int) -> int:
        if i == len(grid) or j == len(grid[0]):
            return float("inf")
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return grid[i][j]
        return grid[i][j] + min(
            self.calculate(grid, i + 1, j), self.calculate(grid, i, j + 1)
        )

    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.calculate(grid, 0, 0)
```

### Approach 2: Dynamic Programming 2D
내 코드랑 비슷하다. 
```py
class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j != n - 1:
                    dp[i][j] = grid[i][j] + dp[i][j + 1]
                elif j == n - 1 and i != m - 1:
                    dp[i][j] = grid[i][j] + dp[i + 1][j]
                elif j != n - 1 and i != m - 1:
                    dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
                else:
                    dp[i][j] = grid[i][j]
        return dp[0][0]
```

### Approach 3: Dynamic Programming 1D
- 1D 배열 (dp) 하나만 사용하여 공간 복잡도를 O(w)로 줄인 Bottom-Up DP 으로 해결
#### 핵심 아이디어
- dp[j]는 현재 행에서 (j열부터 오른쪽 끝까지) 최소 경로 합을 저장
- 오른쪽 아래에서 왼쪽 위로(Bottom-Up) 계산
- 아래쪽(dp[j])과 오른쪽(dp[j+1]) 중 최소값을 선택하여 grid[i][j]에 더함
#### 작동 방식
- 마지막 행은 오른쪽에서만 이동 가능 → dp[j] = grid[i][j] + dp[j+1]
- 마지막 열은 아래쪽에서만 이동 가능 → dp[j] = grid[i][j] + dp[j]
- 나머지는 아래쪽 or 오른쪽 중 작은 값 선택 → dp[j] = grid[i][j] + min(dp[j], dp[j+1])
```py
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [0 for _ in range(len(grid[0]))]
        for i in range(len(grid) - 1, -1, -1):   # 행을 아래에서 위로 이동
            for j in range(len(grid[0]) - 1, -1, -1):  # 열을 오른쪽에서 왼쪽으로 이동
                if i == len(grid) - 1 and j != len(grid[0]) - 1:
                    dp[j] = grid[i][j] + dp[j + 1]
                elif j == len(grid[0]) - 1 and i != len(grid) - 1:
                    dp[j] = grid[i][j] + dp[j]
                elif i != len(grid) - 1 and j != len(grid[0]) - 1:
                    dp[j] = grid[i][j] + min(dp[j], dp[j + 1])
                else:
                    dp[j] = grid[i][j]
        return dp[0]
```

### Approach 4: Dynamic Programming (Without Extra Space)
내 코드랑 거의 똑같다
```py
# Python solution
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in reversed(range(len(grid))):
            for j in reversed(range(len(grid[0]))):
                if i == len(grid) - 1 and j != len(grid[0]) - 1:
                    grid[i][j] += grid[i][j + 1]
                elif j == len(grid[0]) - 1 and i != len(grid) - 1:
                    grid[i][j] += grid[i + 1][j]
                elif j != len(grid[0]) - 1 and i != len(grid) - 1:
                    grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])
        return grid[0][0]
```

### Approach 5:
```py
```