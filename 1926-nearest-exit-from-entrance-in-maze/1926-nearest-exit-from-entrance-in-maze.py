class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        garo = len(maze[0])
        sero = len(maze)

        q = deque()
        dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오 아 왼 위 방향으로 회전
        checked = defaultdict(bool)

        q.append(entrance + [0])

        while q:
            cx, cy, cnt = q.popleft()  # current x, y
            if checked[(cx, cy)]:
                continue
            for dx, dy in dxdy:
                nx = cx + dx
                ny = cy + dy

                # 범위 내에 있으면
                if nx >= 0 and nx < sero and ny >= 0 and ny < garo:
                    # 막다른 벽이 아니면
                    if maze[nx][ny] != "+":
                        q.append([nx, ny, cnt + 1])
                elif cnt != 0:  # 이동은 무조건 해야해
                    return cnt
            checked[(cx, cy)] = True
        return -1