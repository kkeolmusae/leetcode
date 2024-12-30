​# 풀이
- Difficulty:  Medium
- Topic:  Matrix
- Elapsed Time:  (다른 컴퓨터에서 풀었어서 시간 정보가 없다)
- Status:  O (2 times)
- Memo:  다른 컴퓨터에서 풀었어서 메모가 없는데 어렵지 않게 풀었던 것 같다.

## 내 풀이
```py
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 가로, 세로, 3x3 사각형을 모두 확인해야 함
        SIZE = 9

        def checkRow(row: int) -> bool:
            rowSet = set()
            for col in range(SIZE):
                if board[row][col] == ".":
                    continue
                if board[row][col] in rowSet:
                    return False
                rowSet.add(board[row][col])
            return True

        def checkCol(col: int) -> bool:
            colSet = set()
            for row in range(SIZE):
                if board[row][col] == ".":
                    continue
                if board[row][col] in colSet:
                    return False
                colSet.add(board[row][col])
            return True

        def checkSquare(row: int, col: int) -> bool:
            squareSet = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in squareSet:
                        return False
                    squareSet.add(board[i][j])
            return True

        for i in range(SIZE):
            if not checkRow(i):  # 가로 체크
                return False
            if not checkCol(i):  # 세로 체크
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                # 0, 0 / 0, 3 / 0, 6 / 3, 0 / 3, 3 / 3, 6 / 6, 0 / 6, 3 / 6, 6 체크
                if not checkSquare(i, j):
                    return False
        return True
```

## 다른 풀이
### Approach 1:
```py
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