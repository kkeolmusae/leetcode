# 풀이
- Difficulty:  Medium
- Topic:  Multidimensional DP
- Elapsed Time:  10m
- Status:  O 
- Approach:  이전 결과값으로 현재의 결과값을 구해야한다는 부분에서 DP로 접근해서 풀었다.
- Memo:  살짝 헷갈릴수도 있긴 한데 어렵지 않았다.

## 내 풀이
```py
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        h = len(triangle)  # 높이
        for i in range(1, h):  # 두번째층부터 시작
            for j in range(len(triangle[i])):  # 층의 왼쪽부터 시작 
                # 가장 왼쪽 -> 바로 위에꺼 더하기
                if j - 1 < 0:  
                    triangle[i][j] += triangle[i - 1][j]
                # 가장 오른쪽꺼 -> 바로 위에왼쪽꺼
                elif j >= len(triangle[i - 1]):  
                    triangle[i][j] += triangle[i - 1][j - 1]
                # 바로 위랑 위에왼쪽이랑 비교해서 둘중 작은거 골라서 더하기
                else:
                    triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        # 가장 아래층 숫자중에 제일 작은 숫자
        return min(triangle[h - 1])
```

## 다른 풀이
### Approach 1: Dynamic Programming (Bottom-up: In-place)
```py
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(1, len(triangle)):  # 두 번째 행부터 마지막 행까지 반복
            for col in range(row + 1):  # 현재 행의 모든 열을 순회
                smallest_above = math.inf  # 위에서 내려올 수 있는 최소 값을 저장할 변수
                if col > 0:  # 왼쪽 대각선 위에서 내려오는 경우
                    smallest_above = triangle[row - 1][col - 1]
                if col < row:  # 바로 위에서 내려오는 경우
                    smallest_above = min(smallest_above, triangle[row - 1][col])
                triangle[row][col] += smallest_above  # 현재 위치의 값에 최소값을 더함
        return min(triangle[-1])  # 마지막 행에서 최소값을 반환

```

### Approach 2: Dynamic Programming (Bottom-up: Auxiliary Space)
```py
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev_row = triangle[0]  # 첫 번째 행을 이전 행으로 설정
        for row in range(1, len(triangle)):  # 두 번째 행부터 마지막 행까지 반복
            curr_row = []  # 현재 행의 값을 저장할 리스트
            for col in range(row + 1):  # 현재 행의 모든 열을 순회
                smallest_above = math.inf  # 위에서 내려올 수 있는 최소 값을 저장할 변수
                if col > 0:  # 왼쪽 대각선 위에서 내려오는 경우
                    smallest_above = prev_row[col - 1]
                if col < row:  # 바로 위에서 내려오는 경우
                    smallest_above = min(smallest_above, prev_row[col])
                curr_row.append(triangle[row][col] + smallest_above)  # 최소값을 더한 값을 저장
            prev_row = curr_row  # 현재 행을 이전 행으로 업데이트
        return min(prev_row)  # 마지막 행에서 최소값을 반환

```

### Approach 3: Dynamic Programming (Bottom-up: Flip Triangle Upside Down)
```py
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        below_row = triangle[-1]  # 마지막 행을 초기 값으로 설정
        n = len(triangle)
        for row in reversed(range(n - 1)):  # 아래에서 위로 이동
            curr_row = []  # 현재 행의 최소 경로 값을 저장할 리스트
            for col in range(row + 1):  # 현재 행의 모든 열을 순회
                smallest_below = min(below_row[col], below_row[col + 1])  # 아래 두 개 중 최소값 선택
                curr_row.append(triangle[row][col] + smallest_below)  # 현재 값에 최소값을 더함
            below_row = curr_row  # 현재 행을 다음 반복에서 아래 행으로 사용
        return below_row[0]  # 최종적으로 맨 위 값 반환

```

### Approach 4: Memoization (Top-Down)
```py
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @lru_cache(maxsize=None)  # 메모이제이션을 위한 캐시 적용
        def min_path(row, col):
            path = triangle[row][col]  # 현재 위치의 값
            if row < len(triangle) - 1:  # 마지막 행이 아니면 아래 두 개 중 최소값 선택
                path += min(min_path(row + 1, col), min_path(row + 1, col + 1))
            return path

        return min_path(0, 0)  # 맨 위에서 시작하여 최소 경로 반환
```