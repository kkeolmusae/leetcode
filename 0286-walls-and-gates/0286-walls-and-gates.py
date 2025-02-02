class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        EMPTY = 2147483647  # 빈공간
        height = len(rooms)
        width = len(rooms[0])
        dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오 아 왼 위 방향으로 회전

        q = deque()
        for h in range(height):
            for w in range(width):
                if rooms[h][w] == 0:  # gate
                    q.append((h, w))
        if not q:
            return rooms

        while q:
            h, w = q.popleft()
            for dy, dx in dxdy:
                ny = dy + h
                nx = dx + w
                if (
                    0 <= ny
                    and ny < height
                    and 0 <= nx
                    and nx < width
                    and rooms[ny][nx] == EMPTY
                ):
                    rooms[ny][nx] = rooms[h][w] + 1
                    q.append((ny, nx))
        return rooms