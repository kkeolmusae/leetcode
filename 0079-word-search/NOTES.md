# 풀이
- Difficulty:  Medium
- Topic:  Backtracking
- Elapsed Time:  30m
- Status:  O
- Memo: 풀긴 풀었는데 시간 초과했다.

## 내 풀이
```py
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우, 하, 좌, 상 방향

        def backtracking(x: int, y: int, idx: int) -> bool:
            if idx == len(word):  # 단어를 모두 찾은 경우
                return True

            # 찾고자 하는 문자가 아니라면 False
            if (
                x < 0
                or x >= len(board)
                or y < 0
                or y >= len(board[0])
                or board[x][y] != word[idx]
            ):
                return False

            # 현재 문자를 사용하고 탐색
            temp = board[x][y]
            board[x][y] = False  # 방문 표시
            for dx, dy in dxdy:
                if backtracking(x + dx, y + dy, idx + 1):
                    return True
            board[x][y] = temp  # 복구
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:  # 시작 문자 찾기
                    if backtracking(i, j, 0):
                        return True
        return False
```

## 다른 풀이
### Approach 1: Backtracking
```py
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 행과 열의 크기 저장
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        # 보드의 모든 위치를 순회하며 단어 탐색 시작
        for row in range(self.ROWS):
            for col in range(self.COLS):
                # 단어를 찾으면 True 반환
                if self.backtrack(row, col, word):
                    return True

        # 모든 위치를 탐색했지만 단어를 찾지 못한 경우 False 반환
        return False

    def backtrack(self, row: int, col: int, suffix: str) -> bool:
        # 종료 조건: 단어의 모든 문자를 찾은 경우
        if len(suffix) == 0:
            return True

        # 현재 상태를 확인하여 백트래킹 가능 여부 판단
        if (
            row < 0  # 행 범위를 벗어남
            or row == self.ROWS  # 행 범위를 벗어남
            or col < 0  # 열 범위를 벗어남
            or col == self.COLS  # 열 범위를 벗어남
            or self.board[row][col] != suffix[0]  # 현재 위치의 문자가 단어의 첫 문자와 일치하지 않음
        ):
            return False

        # 현재 위치를 방문했음을 표시
        ret = False
        self.board[row][col] = "#"

        # 4개의 이웃 방향(우, 하, 좌, 상)을 탐색
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            # 재귀적으로 다음 문자를 탐색
            ret = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
            # 탐색 중 단어를 찾으면 반복 종료
            if ret:
                break

        # 탐색 완료 후 현재 위치를 원래 문자로 복구 (백트래킹)
        self.board[row][col] = suffix[0]

        # 모든 방향을 탐색한 결과 반환
        return ret

```

### Approach 2:
```py
```

### Approach 3:
```py
```

### Approach 4:
```py
```

### Approach 5:
```py
```