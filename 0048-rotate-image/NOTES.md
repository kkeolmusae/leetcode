# 풀이
- Difficulty: Medium
- Topic: Matrix
- Elapsed Time:  10m
- Status:  O (2 times)
- Memo: 배열을 회전시키는 코드를 가져다 사용함. for 문을 어디까지 돌릴지에 대한 이해와 배열을 회전시키는 방법만 알면 금방 풀리는 문제

## 내 풀이
처음 풀었을때는 새로운 배열을 할당하지 않고 하는 방법이 떠오르지 않았는데, 이번에는 새 배열 할당 안하고 품
```py
class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)  # 행렬의 크기 계산 (nxn 행렬)
        for i in range(n // 2 + n % 2):  # 바깥쪽에서 안쪽으로 이동 (반만 순회)
            for j in range(n // 2):  # 열의 절반만 순회 (나머지는 대칭적으로 처리)
                # 4개의 값을 회전하며 교환
                tmp = matrix[j][n - i - 1]  # 오른쪽 위 값을 임시 저장
                matrix[j][n - i - 1] = matrix[i][j]  # 왼쪽 위 값을 오른쪽 위로 이동
                matrix[i][j] = matrix[n - j - 1][i]  # 왼쪽 아래 값을 왼쪽 위로 이동
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]  # 오른쪽 아래 값을 왼쪽 아래로 이동
                matrix[n - i - 1][n - j - 1] = tmp  # 임시 저장한 값을 오른쪽 아래로 이동

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
