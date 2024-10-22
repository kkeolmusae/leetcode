class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()  # 땅 위치
        cnt = 0

        garo = len(grid[0])
        sero = len(grid)

        # 오 아 왼 위 방향으로 회전
        dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(sero):
            for j in range(garo):
                if grid[i][j] == "1":
                    q.append((i, j))
                    cnt += 1
                    while q:
                        x, y = q.popleft()
                        if grid[x][y] == "1":  # 땅인 경우에
                            grid[x][y] = "2"  # 확인처리
                            for idx in range(4):  # 동서남북 체크
                                nx = x + dxdy[idx][0]
                                ny = y + dxdy[idx][1]

                                if nx >= 0 and nx < sero and ny >= 0 and ny < garo:
                                    if grid[nx][ny] == "1":  # 주변에 땅이 있으면
                                        q.append((nx, ny))  # q 에 넣어둠
        return cnt
