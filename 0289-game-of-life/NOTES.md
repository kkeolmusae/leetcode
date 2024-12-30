# 풀이
- Difficulty:  Medium
- Topic:  Matrix
- Elapsed Time:  18m
- Status:  O
- Memo:  문제 그대로 구현하면 되는 거였어서 어렵지 않았음. 

## 내 풀이
```py
class Solution:
    # 방향 벡터: 동, 남동, 남, 남서, 서, 북서, 북, 북동
    dxdy = [
        (0, 1),    # 동쪽
        (1, 1),    # 남동쪽
        (1, 0),    # 남쪽
        (1, -1),   # 남서쪽
        (0, -1),   # 서쪽
        (-1, -1),  # 북서쪽
        (-1, 0),   # 북쪽
        (-1, 1),   # 북동쪽
    ]

    def gameOfLife(self, board: List[List[int]]) -> None:
        col = len(board[0])  # 열의 개수
        row = len(board)  # 행의 개수
        mem = defaultdict(list)  # 다음 상태를 저장할 딕셔너리

        # 각 셀의 상태와 이웃 셀의 상태를 확인
        for i in range(row):  # 행 순회
            for j in range(col):  # 열 순회
                live_neighbor = 0  # 살아있는 이웃 셀의 수
                dead_neighbor = 0  # 죽어있는 이웃 셀의 수

                # 현재 셀이 살아있는 경우
                if board[i][j] == 1:
                    for x, y in self.dxdy:  # 8개의 방향 확인
                        nx = x + i  # 새로운 x 좌표
                        ny = y + j  # 새로운 y 좌표
                        if nx >= 0 and nx < row and ny >= 0 and ny < col:  # 유효한 좌표인지 확인
                            if board[nx][ny] == 0:  # 이웃 셀이 죽어있다면
                                dead_neighbor += 1
                            else:  # 이웃 셀이 살아있다면
                                live_neighbor += 1

                    # 살아있는 이웃의 수에 따라 상태 결정
                    if live_neighbor < 2 or live_neighbor > 3:  # 과소/과잉으로 인해 사망
                        mem[0].append((i, j))
                    else:  # 다음 세대에도 생존
                        mem[1].append((i, j))
                # 현재 셀이 죽어있는 경우
                else:
                    for x, y in self.dxdy:  # 8개의 방향 확인
                        nx = x + i  # 새로운 x 좌표
                        ny = y + j  # 새로운 y 좌표
                        if nx >= 0 and nx < row and ny >= 0 and ny < col:  # 유효한 좌표인지 확인
                            if board[nx][ny] == 0:  # 이웃 셀이 죽어있다면
                                dead_neighbor += 1
                            else:  # 이웃 셀이 살아있다면
                                live_neighbor += 1

                    # 이웃 셀의 상태에 따라 상태 결정
                    if live_neighbor == 3:  # 번식 조건 만족
                        mem[1].append((i, j))
                    else:  # 계속 죽어 있음
                        mem[0].append((i, j))

        # 기록된 상태로 셀 업데이트
        for i, j in mem[0]:  # 죽은 셀로 업데이트
            board[i][j] = 0
        for i, j in mem[1]:  # 살아있는 셀로 업데이트
            board[i][j] = 1

```

## 다른 풀이
### Approach 1: O(mn) Space Solution
```py
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # 이웃 셀의 상대적 좌표를 정의 (8방향)
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

        rows = len(board)  # 행의 개수
        cols = len(board[0])  # 열의 개수

        # 원본 보드의 복사본 생성
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

        # 보드의 각 셀을 순회
        for row in range(rows):
            for col in range(cols):

                # 각 셀의 살아있는 이웃 수를 계산
                live_neighbors = 0
                for neighbor in neighbors:
                    # 이웃 셀의 좌표 계산
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    # 이웃 셀이 보드 범위 내에 있고, 복사본 기준으로 살아있는 경우
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and (copy_board[r][c] == 1):
                        live_neighbors += 1

                # 규칙 1 또는 규칙 3 적용: 살아있는 셀이 과소 또는 과잉으로 인해 사망
                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                # 규칙 4 적용: 죽어 있는 셀이 번식
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1

```

### Approach 2: O(1) Space Solution
```py
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # 이웃 셀의 상대적 좌표를 정의 (8방향)
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

        rows = len(board)  # 행의 개수
        cols = len(board[0])  # 열의 개수

        # 보드의 각 셀을 순회
        for row in range(rows):
            for col in range(cols):

                # 각 셀의 살아있는 이웃 수를 계산
                live_neighbors = 0
                for neighbor in neighbors:
                    # 이웃 셀의 좌표 계산
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    # 이웃 셀이 보드 범위 내에 있고, 원래 살아있는 경우(abs(board[r][c]) == 1)
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and abs(board[r][c]) == 1:
                        live_neighbors += 1

                # 규칙 1 또는 규칙 3 적용: 살아있는 셀이 과소 또는 과잉으로 인해 사망
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    # -1은 셀이 현재는 죽었지만 원래는 살아있었음을 의미
                    board[row][col] = -1
                # 규칙 4 적용: 죽어 있는 셀이 번식
                if board[row][col] == 0 and live_neighbors == 3:
                    # 2는 셀이 현재는 살아있지만 원래는 죽어있었음을 의미
                    board[row][col] = 2

        # 보드를 최종적으로 업데이트
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    # 양수는 현재 살아있는 셀을 의미
                    board[row][col] = 1
                else:
                    # 음수 또는 0은 현재 죽어있는 셀을 의미
                    board[row][col] = 0
```