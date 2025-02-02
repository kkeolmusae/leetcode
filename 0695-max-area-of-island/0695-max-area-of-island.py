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