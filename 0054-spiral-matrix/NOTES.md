# 풀이
- Difficulty:  Medium
- Topic:  Matrix
- Elapsed Time:  20m
- Status:  O (2 times)
- Memo: 문제 자체는 안어려웠음. 가로세로가 좀 헷갈릴뿐,,,,

## 내 풀이
```py
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        checked = math.inf
        height = len(matrix)  # 세로
        width = len(matrix[0])  # 가로

        total = height * width  # 전체 숫자 개수
        x, y = 0, 0

        direction = 0  # 방향
        dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오 아 왼 위 방향으로 회전

        while total:
            result.append(matrix[x][y])  # 숫자 저장
            matrix[x][y] = checked  # 방문 처리
            total -= 1  # 전체 개수 감소
            nx, ny = x + dxdy[direction][0], y + dxdy[direction][1]  # 다음 좌표

            # 회전해야하는 경우
            if (
                nx >= height
                or nx < 0
                or ny < 0
                or ny >= width
                or matrix[nx][ny] == checked
            ):
                direction = (direction + 1) % 4
                nx, ny = x + dxdy[direction][0], y + dxdy[direction][1]
            x, y = nx, ny
        return result

```

## 다른 풀이
### Approach 1: Set Up Boundaries
```py
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []  # 결과를 저장할 리스트
        rows, columns = len(matrix), len(matrix[0])  # 행과 열의 크기 저장
        up = left = 0  # 상단, 왼쪽 경계 초기화
        right = columns - 1  # 오른쪽 경계 초기화
        down = rows - 1  # 하단 경계 초기화

        # 결과 리스트에 모든 숫자가 담길 때까지 반복
        while len(result) < rows * columns:
            # 1. 왼쪽에서 오른쪽으로 순회 (위쪽 행을 순회)
            for col in range(left, right + 1):
                result.append(matrix[up][col])  # 현재 위쪽 행의 각 열을 순차적으로 결과에 추가

            # 2. 위에서 아래로 순회 (오른쪽 열을 순회)
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])  # 현재 오른쪽 열의 각 행을 순차적으로 결과에 추가

            # 3. 오른쪽에서 왼쪽으로 순회 (하단 행을 순회)
            if up != down:  # 상단과 하단이 같지 않다면
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])  # 현재 하단 행의 각 열을 역순으로 결과에 추가

            # 4. 아래에서 위로 순회 (왼쪽 열을 순회)
            if left != right:  # 왼쪽과 오른쪽이 같지 않다면
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])  # 현재 왼쪽 열의 각 행을 역순으로 결과에 추가

            # 상, 하, 좌, 우 경계를 한 칸씩 좁힘
            left += 1
            right -= 1
            up += 1
            down -= 1

        return result  # 나선형 순서대로 저장된 결과 반환

```

### Approach 2: Mark Visited Elements
```py
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        VISITED = 101  # 이미 방문한 셀을 표시할 값 (101로 설정)
        rows, columns = len(matrix), len(matrix[0])  # 행과 열의 크기 저장
        # 네 방향: 오른쪽 (0, 1), 아래쪽 (1, 0), 왼쪽 (0, -1), 위쪽 (-1, 0)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # 초기 방향은 오른쪽으로 설정 (0번째 방향)
        current_direction = 0
        
        # 방향을 바꿀 때마다 change_direction을 증가시켜 4번의 방향을 모두 돌게 설정
        change_direction = 0
        
        # 현재 위치 (row, col)로 설정 (시작 위치는 (0, 0))
        row = col = 0
        
        # 첫 번째 원소를 result에 추가하고, 해당 셀을 VISITED로 표시
        result = [matrix[0][0]]
        matrix[0][0] = VISITED

        # 방향을 네 번 바꾸면 종료 (나선형 순회 완료)
        while change_direction < 4:
            while True:
                # 현재 방향에 맞춰 다음에 이동할 셀을 계산
                next_row = row + directions[current_direction][0]
                next_col = col + directions[current_direction][1]

                # 다음 셀이 범위를 벗어나면 종료
                if not (0 <= next_row < rows and 0 <= next_col < columns):
                    break

                # 다음 셀이 이미 방문된 셀이면 종료
                if matrix[next_row][next_col] == VISITED:
                    break

                # 위 조건에 걸리지 않으면 방향을 바꾸지 않고 계속 진행
                change_direction = 0
                # 현재 위치를 업데이트
                row, col = next_row, next_col
                # 해당 위치의 값을 결과에 추가하고, 방문 표시
                result.append(matrix[row][col])
                matrix[row][col] = VISITED

            # 방향을 바꿔서 다음 방향으로 설정
            current_direction = (current_direction + 1) % 4
            # 방향을 바꾼 횟수 증가
            change_direction += 1

        return result  # 나선형 순회 결과를 반환
```