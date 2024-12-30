class Solution:
    dxdy = [
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    ]  # 오 아 왼 위 방향으로 회전

    def gameOfLife(self, board: List[List[int]]) -> None:
        dead_cell = []
        life_cell = []
        col = len(board[0])
        row = len(board)
        mem = defaultdict(list)

        for i in range(row):  # 가로줄
            for j in range(col):  # 세로줄
                live_neighbor = 0
                dead_neighbor = 0
                if board[i][j] == 1:
                    for x, y in self.dxdy:
                        nx = x + i
                        ny = y + j
                        if nx >= 0 and nx < row and ny >= 0 and ny < col:
                            if board[nx][ny] == 0:
                                dead_neighbor += 1
                            else:
                                live_neighbor += 1
                    if live_neighbor < 2 or live_neighbor > 3:
                        mem[0].append((i, j))
                    else:
                        mem[1].append((i, j))
                else:
                    for x, y in self.dxdy:
                        nx = x + i
                        ny = y + j
                        if nx >= 0 and nx < row and ny >= 0 and ny < col:
                            if board[nx][ny] == 0:
                                dead_neighbor += 1
                            else:
                                live_neighbor += 1
                    if live_neighbor == 3:
                        mem[1].append((i, j))
                    else:
                        mem[0].append((i, j))

        for i, j in mem[0]:
            board[i][j] = 0
        for i, j in mem[1]:
            board[i][j] = 1