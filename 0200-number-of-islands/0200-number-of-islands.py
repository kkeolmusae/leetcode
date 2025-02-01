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
