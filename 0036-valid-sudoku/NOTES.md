# 풀이
- Difficulty:  Medium
- Topic:  Matrix
- Elapsed Time:  8m
- Status:  O (2 times)
- Memo: 쉬운 문제고 이전에 풀었던거라 금방 해결했다.

## 내 풀이
문제 자체는 금방 해결했는데 좀 더 개선할 수 있지 않을까 하는 생각이 든다
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
### Approach 1: Hash Set
```py
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        # Use hash set to record the status
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]  # 현재 위치의 숫자
                # 빈칸이면 다음으로
                if val == ".":
                    continue

                # 가로에 현재 숫자있는지 확인
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # 세로에 현재 숫자있는지 확인
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # 박스 체크
                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True
```

### Approach 2: Array of Fixed Length
공간 복잡도 측면에서 별로 인듯..?
```py
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9  # 보드의 크기 (9x9)

        # 각 행, 열, 박스를 추적하기 위한 상태 배열
        rows = [[0] * N for _ in range(N)]  # 행에 있는 숫자 상태
        cols = [[0] * N for _ in range(N)]  # 열에 있는 숫자 상태
        boxes = [[0] * N for _ in range(N)]  # 3x3 박스에 있는 숫자 상태

        # 보드 순회
        for r in range(N):
            for c in range(N):
                # 현재 위치에 숫자가 없으면 건너뜀
                if board[r][c] == ".":
                    continue

                pos = int(board[r][c]) - 1  # 숫자를 0 기반 인덱스로 변환

                # 행에서 숫자 중복 체크
                if rows[r][pos] == 1:  # 이미 존재하면 False 반환
                    return False
                rows[r][pos] = 1  # 숫자 추가

                # 열에서 숫자 중복 체크
                if cols[c][pos] == 1:  # 이미 존재하면 False 반환
                    return False
                cols[c][pos] = 1  # 숫자 추가

                # 박스(3x3)에서 숫자 중복 체크
                idx = (r // 3) * 3 + c // 3  # 현재 좌표의 박스 인덱스 계산
                if boxes[idx][pos] == 1:  # 이미 존재하면 False 반환
                    return False
                boxes[idx][pos] = 1  # 숫자 추가

        # 모든 조건을 만족하면 True 반환
        return True
```

### Approach 3: Bitmasking
비트마스킹을 활용하여 숫자를 shift 하는 방식으로 status를 저장하는 방법
```py
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9  # 보드의 크기 (9x9)
        
        # 각 행, 열, 박스를 추적하기 위한 상태 배열 (비트마스크 사용)
        rows = [0] * N  # 행에 있는 숫자 상태를 비트로 저장
        cols = [0] * N  # 열에 있는 숫자 상태를 비트로 저장
        boxes = [0] * N  # 3x3 박스에 있는 숫자 상태를 비트로 저장

        # 보드 순회
        for r in range(N):
            for c in range(N):
                # 현재 위치가 비어 있다면 건너뜀
                if board[r][c] == ".":
                    continue

                pos = int(board[r][c]) - 1  # 숫자를 0 기반 비트 인덱스로 변환

                # 행에서 숫자 중복 체크
                if rows[r] & (1 << pos):  # 해당 비트가 이미 켜져 있으면 중복
                    return False
                rows[r] |= 1 << pos  # 숫자 추가 (비트 켜기)

                # 열에서 숫자 중복 체크
                if cols[c] & (1 << pos):  # 해당 비트가 이미 켜져 있으면 중복
                    return False
                cols[c] |= 1 << pos  # 숫자 추가 (비트 켜기)

                # 박스(3x3)에서 숫자 중복 체크
                idx = (r // 3) * 3 + c // 3  # 현재 좌표의 박스 인덱스 계산
                if boxes[idx] & (1 << pos):  # 해당 비트가 이미 켜져 있으면 중복
                    return False
                boxes[idx] |= 1 << pos  # 숫자 추가 (비트 켜기)

        # 모든 조건을 만족하면 True 반환
        return True
```