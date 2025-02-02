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