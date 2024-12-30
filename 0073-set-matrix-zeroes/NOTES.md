# 풀이
- Difficulty:  Medium
- Topic:  Matrix
- Elapsed Time:  8m
- Status:  O (2 times)
- Memo: 안어려웠음. 가로세로 헷갈린거 빼고 수월했음

## 내 풀이
```py
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)  # 행의 개수
        cols = len(matrix[0])  # 열의 개수

        zero = set()  # 0의 좌표를 저장할 집합
        for i in range(rows):  # 행 순회
            for j in range(cols):  # 열 순회
                if matrix[i][j] == 0:  # 0인 경우
                    zero.add((i, j))  # 좌표 저장

        for i, j in zero:  # 0의 좌표를 순회
            for idx in range(rows):  # 해당 열을 0으로 설정
                matrix[idx][j] = 0
            for idx in range(cols):  # 해당 행을 0으로 설정
                matrix[i][idx] = 0
```

## 다른 풀이
### Approach 1: Additional Memory Approach
```py
class Solution(object):
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # 행렬의 행(row) 개수와 열(column) 개수를 구합니다.
        R = len(matrix)  # 행의 개수
        C = len(matrix[0])  # 열의 개수
        rows, cols = set(), set()  # 0으로 설정할 행과 열을 저장할 집합 생성

        # 1단계: 0이 포함된 행과 열을 기록
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:  # 현재 위치가 0이라면
                    rows.add(i)  # 행 번호를 rows 집합에 추가
                    cols.add(j)  # 열 번호를 cols 집합에 추가

        # 2단계: 기록된 행과 열을 기준으로 행렬 요소를 0으로 설정
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:  # 현재 행 또는 열이 기록된 집합에 있다면
                    matrix[i][j] = 0  # 해당 위치를 0으로 설정
```

### Approach 2: O(1) Space, Efficient Solution
```py
class Solution(object):
    def setZeroes(self, matrix: List[List[int]]) -> None:
        is_col = False  # 첫 번째 열을 0으로 설정할지 여부를 저장하는 변수
        R = len(matrix)  # 행(row) 개수
        C = len(matrix[0])  # 열(column) 개수
        
        # 1단계: 첫 번째 행과 첫 번째 열을 이용해 0 상태 기록
        for i in range(R):
            # 첫 번째 열에서 0이 발견되면 `is_col`을 True로 설정
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):  # 첫 번째 열은 제외하고 나머지 열을 확인
                if matrix[i][j] == 0:  # 0을 발견하면
                    matrix[0][j] = 0  # 해당 열의 첫 번째 행 요소를 0으로 설정
                    matrix[i][0] = 0  # 해당 행의 첫 번째 열 요소를 0으로 설정

        # 2단계: 첫 번째 행과 열을 참조하여 나머지 요소를 업데이트
        for i in range(1, R):  # 첫 번째 행과 열은 나중에 처리하므로 제외
            for j in range(1, C):
                if matrix[i][0] == 0 or matrix[0][j] == 0:  # 행 또는 열의 첫 번째 요소가 0이라면
                    matrix[i][j] = 0  # 현재 요소를 0으로 설정

        # 3단계: 첫 번째 행 처리
        if matrix[0][0] == 0:  # 첫 번째 행의 첫 번째 요소가 0이라면
            for j in range(C):
                matrix[0][j] = 0  # 첫 번째 행 전체를 0으로 설정

        # 4단계: 첫 번째 열 처리
        if is_col:  # `is_col`이 True라면
            for i in range(R):
                matrix[i][0] = 0  # 첫 번째 열 전체를 0으로 설정
```
