# 풀이
- Difficulty:  Medium
- Topic:  Array / String
- Elapsed Time:  10m
- Status:  O
- Memo: 생각보다 큰 어려움없이 풀었다. 

## 내 풀이
go_down 이라는 플래그를 사용하여 방향을 조절하였다.
```py
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = defaultdict(list)  # 파이썬의 문자열 불변 특성 때문에 문자열가 아닌 list를 사용했다.
        lidx = 0
        go_down = True

        if numRows == 1:
            return s

        for idx in range(len(s)):
            l[lidx].append(s[idx])  # 문자 추가하기
            lidx = lidx + 1 if go_down else lidx - 1

            if lidx >= numRows or lidx < 0:  # 끝에 다달았으면
                lidx = lidx + 2 if not go_down else lidx - 2
                if go_down == True:
                    go_down = False
                else:
                    go_down = True

        result = ""
        for idx in range(numRows):
            result += "".join(l[idx])
        return result

```

## 다른 풀이
### Approach 1: Simulate Zig-Zag Movement
이차원 배열을 써서 풀었는데 코드보면 내꺼보다 어렵게 품
```py
class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        # 행의 개수가 1이면 문자열을 변환하지 않고 그대로 반환
        if num_rows == 1:
            return s

        n = len(s)  # 문자열의 길이
        # Z자 모양의 패턴에서 한 섹션의 길이를 계산
        sections = ceil(n / (2 * num_rows - 2.0))
        # 필요한 열의 개수를 계산
        num_cols = sections * (num_rows - 1)

        # 행렬을 생성하여 공백(" ")으로 초기화
        matrix = [[" "] * num_cols for _ in range(num_rows)]

        # 행렬의 현재 위치를 나타내는 변수들
        curr_row, curr_col = 0, 0
        curr_string_index = 0  # 현재 처리 중인 문자열의 인덱스

        # 행렬을 Z자 패턴으로 순회하며 문자열의 문자를 채워넣음
        while curr_string_index < n:
            # 아래로 이동하면서 문자 채우기
            while curr_row < num_rows and curr_string_index < n:
                matrix[curr_row][curr_col] = s[curr_string_index]
                curr_row += 1
                curr_string_index += 1

            # 아래로 이동이 끝난 후, 행과 열 위치를 조정
            curr_row -= 2
            curr_col += 1

            # 대각선 위로 이동하면서 문자 채우기
            while (
                curr_row > 0 and curr_col < num_cols and curr_string_index < n
            ):
                matrix[curr_row][curr_col] = s[curr_string_index]
                curr_row -= 1
                curr_col += 1
                curr_string_index += 1

        # 행렬을 순회하며 문자열을 생성
        answer = ""
        for row in matrix:
            answer += "".join(row)

        # 공백을 제거하고 결과 반환
        return answer.replace(" ", "")

```

### Approach 2: String Traversal
점프 패턴을 분석하여 정답을 도출함
```py
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Z자 패턴에서 행의 개수가 1이면 변환 없이 원본 문자열 반환
        if numRows == 1:
            return s

        answer = []  # 결과를 저장할 리스트
        n = len(s)  # 입력 문자열의 길이
        chars_in_section = 2 * (numRows - 1)  # Z자 패턴에서 한 섹션의 문자 수

        # 각 행을 순회하며 Z자 패턴에 맞게 문자를 추가
        for curr_row in range(numRows):
            index = curr_row  # 현재 행의 첫 번째 문자의 인덱스
            while index < n:
                # 현재 행의 문자를 결과 리스트에 추가
                answer.append(s[index])

                # 첫 번째와 마지막 행이 아닌 경우, 섹션 내의 대각선에 위치한 문자도 추가
                if curr_row != 0 and curr_row != numRows - 1:
                    # 대각선에 있는 문자까지의 거리 계산
                    chars_in_between = chars_in_section - 2 * curr_row
                    second_index = index + chars_in_between

                    # 대각선 문자 인덱스가 문자열 길이를 초과하지 않을 때만 추가
                    if second_index < n:
                        answer.append(s[second_index])

                # 다음 섹션의 동일한 행의 첫 번째 문자로 이동
                index += chars_in_section

        # 리스트를 문자열로 변환하여 반환
        return "".join(answer)

```