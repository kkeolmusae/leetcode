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

        return grid[-1][-1]