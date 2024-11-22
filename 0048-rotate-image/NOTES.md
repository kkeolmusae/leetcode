# 풀이
- Medium
- Matrix
- Time: 5m?
- 이전에 배열을 회전하는걸 해본적이 있어서 그 코드 그대로 가져다 씀. 이런건 외워두는게 좋을듯함.

## 내 풀이
문제에서 새로운 배열을 할당하지말고 기존 배열 그대로 사용하라고 해서 기존 배열을 deep copy해서 해결함
```py
import copy
from typing import List


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)  # 행 길이 계산
        m = len(matrix[0])  # 열 길이 계산
        temp = copy.deepcopy(matrix)  # 임시 배열
        for i in range(n):
            for j in range(m):
                matrix[j][n - i - 1] = temp[i][j]
```

## 다른 풀이
### Approach 1: Rotate Groups of Four Cells
한번에 4개씩 바꾸는 방법. 한번에 4개씩 바꾸다 보니 따로 임시 배열을 할당할 필요가 없음
```py
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
```

### Approach 2: Reverse on the Diagonal and then Reverse Left to Right
신기하고 기똥찬 방법
- 왼쪽위에서 오른쪽 아래로 가는 대각선 값을 제외하고 (i,j) = (j,i) 로 값을 반전시킨후
- 중간배열을 기준으로 좌우값을 반전시키는 방법
```py
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)

    # (0,0), (1,1) 등을 제외하고 자리 바꿈 (1,0) = (0,1)
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # 3차원 배열 기준으로 (1,0), (1,1) 등을 제외하고 자리 바꿈 (0,0) = (2,0)
    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = (
                    matrix[i][-j - 1],
                    matrix[i][j],
                )
```

### Approach 3:
```py
```