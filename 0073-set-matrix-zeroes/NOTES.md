# 풀이
- Medium
- Matrix
- Time: 11m 20s
- 별로 안어려웠음. 가로세로 헷갈린거 빼고 수월했음

## 내 풀이
```py
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        garo = len(matrix[0])
        sero = len(matrix)

        zero = set()  # 0 위치 저장
        for i in range(sero):
            for j in range(garo):
                if matrix[i][j] == 0:
                    zero.add((i, j))

        for i, j in zero:
            for x in range(garo):  # 가로줄 0처리
                matrix[i][x] = 0
            for x in range(sero):  # 세로줄 0처리
                matrix[x][j] = 0
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
