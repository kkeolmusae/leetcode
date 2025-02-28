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