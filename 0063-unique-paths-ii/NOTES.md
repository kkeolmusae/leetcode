# 풀이
- Difficulty:  Medium
- Topic:  Multidimensional DP
- Elapsed Time:  1m
- Status:  O
- Approach:  이전 결과값으로 다음 결과값을 구해야한다는 부분에서 DP로 접근해서 풀었다. 
- Memo:  생각보다 어렵지 않았다. 오랜만에 푼것같은데 금방 풀렸다.

## 내 풀이
- 시작점이면서 돌이 없는 부분은 1로 세팅하고 
- 돌이 있는 부분(`obstacleGrid[i][j] == 1`) 은 넘어가고
- 그게 아니라면 (길이 라면) 왼쪽에서 오는 경우와 위쪽에서 오는 경우의 수를 더하는 방법으로 풀었다.
꽤나 어렵지 않았다.
```py
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        h, w = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                if i == 0 and j == 0 and obstacleGrid[i][j] == 0:
                    dp[i][j] = 1
                elif obstacleGrid[i][j] == 1:
                    continue
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[h - 1][w - 1]
```

## 다른 풀이
### Approach 1: Dynamic Programming
```py
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)  # 행 개수
        n = len(obstacleGrid[0])  # 열 개수

        # 시작 지점에 장애물이 있으면 경로가 없으므로 0 반환
        if obstacleGrid[0][0] == 1:
            return 0

        # 시작 위치(0,0)에서 도착할 수 있는 경우의 수는 1로 설정
        obstacleGrid[0][0] = 1

        # 첫 번째 열 초기화 (위쪽에서 내려오는 경우)
        for i in range(1, m):
            obstacleGrid[i][0] = int(
                obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1
            )

        # 첫 번째 행 초기화 (왼쪽에서 오는 경우)
        for j in range(1, n):
            obstacleGrid[0][j] = int(
                obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1
            )

        # (1,1)부터 끝까지 DP 적용
        # 특정 위치 (i, j)에 도달하는 경우의 수는
        # 위쪽 (i-1, j)에서 오는 경우 + 왼쪽 (i, j-1)에서 오는 경우
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:  # 장애물이 없는 경우
                    obstacleGrid[i][j] = (
                        obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                    )
                else:  # 장애물이 있는 경우 경로가 없으므로 0 설정
                    obstacleGrid[i][j] = 0

        # 최종적으로 도착지점의 값 반환 (도착할 수 있는 경우의 수)
        return obstacleGrid[m - 1][n - 1]

```
