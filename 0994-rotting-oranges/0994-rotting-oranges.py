class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0: 빈셀, 1: fresh, 2: rotten

        q = deque()  # 썩은 오렌지 위치 저장
        fresh_cnt = 0  # 신선한 오렌지 개수 저장
        result = 0  # 걸린 시간

        garo = len(grid[0])
        sero = len(grid)

        dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오 아 왼 위 방향으로 회전
        checked = defaultdict(bool)

        for i in range(sero):
            for j in range(garo):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh_cnt += 1

        while q:
            cx, cy, ctime = q.popleft()  # 현재 x,y,time
            result = max(ctime, result)
            if checked[(cx, cy)]:  # 확인한적있는 곳이면 패스
                continue
            checked[(cx, cy)] = True  # 확인 처리

            for dx, dy in dxdy:
                nx = cx + dx
                ny = cy + dy
                if nx >= 0 and nx < sero and ny >= 0 and ny < garo:  # 범위내
                    if grid[nx][ny] == 1:  # 신선한 과일 발견
                        grid[nx][ny] = 2  # 감염처리
                        q.append((nx, ny, ctime + 1))
                        fresh_cnt -= 1

        if fresh_cnt > 0:  # 신선한게 남아있으면
            return -1
        return result