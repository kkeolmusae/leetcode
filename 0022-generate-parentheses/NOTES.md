# 풀이
- Difficulty:  Medium
- Topic:  Stack
- Elapsed Time:  20m
- Status:  O
- Memo: 풀긴 풀었는데 Stack 안쓰고 Queue 를 써서 Brute Force 로 풀었다. 시간 복잡도도 좀 별로인듯

## 내 풀이
처음에는 모든 경우의 수로 해결하려고 했는데 Memory가 터져서 다시 풀었다. 결국 Brute force 로 풀어서 시간복잡도가 별로다..
```py
class Solution:
    def check(self, n: int, st: str) -> bool:
        # 주어진 문자열이 올바른 괄호 문자열인지 확인하는 함수
        left = 0  # 열린 괄호 "("의 개수
        right = 0  # 닫힌 괄호 ")"의 개수

        for s in st:
            if s == "(":  # 열린 괄호일 경우
                left += 1
            else:  # 닫힌 괄호일 경우
                right += 1

            # 닫힌 괄호가 열린 괄호보다 많거나, 
            # 열린 괄호 또는 닫힌 괄호가 n을 초과하면 유효하지 않음
            if right > left or left > n or right > n:
                return False
        # 열린 괄호와 닫힌 괄호의 개수가 정확히 n이어야 유효
        return right == n

    def generateParenthesis(self, n: int) -> List[str]:
        # n개의 올바른 괄호 조합을 생성하는 함수
        answer = []  # 결과를 저장할 리스트
        queue = deque([""])  # BFS를 위한 큐 초기화 (빈 문자열로 시작)

        while queue:
            curr = queue.popleft()  # 현재 문자열을 가져옴

            # 문자열의 길이가 2 * n이면 유효성 검사 후 추가
            if len(curr) == n * 2:
                if self.check(n, curr):  # 올바른 괄호 문자열인지 확인
                    answer.append(curr)  # 결과 리스트에 추가
                continue
            
            # 열린 괄호 "("를 추가한 경우를 큐에 삽입
            queue.append(curr + "(")
            # 닫힌 괄호 ")"를 추가한 경우를 큐에 삽입
            queue.append(curr + ")")

        return answer  # 모든 올바른 조합 반환

```

## 다른 풀이
### Approach 1: Brute Force
내 코드랑 똑같이 Brute Force로 풀었다. valid 한 문자인지 체크하는 코드만 다르다
```py
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(p_string):
            left_count = 0
            for p in p_string:
                if p == "(":
                    left_count += 1
                else:
                    left_count -= 1

                if left_count < 0:
                    return False

            return left_count == 0

        answer = []
        queue = collections.deque([""])
        while queue:
            cur_string = queue.popleft()

            if len(cur_string) == 2 * n:
                if isValid(cur_string):
                    answer.append(cur_string)
                continue
            queue.append(cur_string + ")")
            queue.append(cur_string + "(")

        return answer
```

### Approach 2: Backtracking, Keep Candidate Valid
백트랙킹으로 해결하는 방법이다. 현재 상태에서 다음상태로 갈때는 append 하고, 이전의 상태로 돌아갈때 pop을 사용하는 것으로 보아 이 방법이 Stack으로 푼 대표적인 케이스가 아닌가 싶다.
(+ 백트랙킹 재밌네)
```py
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 결과를 저장할 리스트
        answer = []

        # 백트래킹 함수 정의
        def backtracking(cur_string, left_count, right_count):
            # 기저 조건: 현재 문자열의 길이가 2 * n일 경우, 결과 리스트에 추가
            if len(cur_string) == 2 * n:
                answer.append("".join(cur_string))  # 리스트를 문자열로 변환하여 저장
                return
            
            # 열린 괄호 "("를 추가할 수 있는 경우
            if left_count < n:
                cur_string.append("(")  # 열린 괄호 추가
                backtracking(cur_string, left_count + 1, right_count)  # 재귀 호출
                cur_string.pop()  # 백트래킹: 상태 복원
            
            # 닫힌 괄호 ")"를 추가할 수 있는 경우 (닫힌 괄호 개수가 열린 괄호보다 적어야 함)
            if right_count < left_count:
                cur_string.append(")")  # 닫힌 괄호 추가
                backtracking(cur_string, left_count, right_count + 1)  # 재귀 호출
                cur_string.pop()  # 백트래킹: 상태 복원

        # 백트래킹 시작
        backtracking([], 0, 0)
        return answer

```

### Approach 3: Divide and Conquer
분할 정복(Divide and Conquer) 접근 방식인데... 헷갈린다 ㅠ
```py
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n이 0일 경우, 빈 문자열만을 반환
        if n == 0:
            return [""]

        # 결과를 저장할 리스트
        answer = []
        # 가능한 왼쪽 괄호의 개수를 반복
        for left_count in range(n):
            # 왼쪽 부분 문자열 생성 (self.generateParenthesis(left_count): 왼쪽에 들어갈 괄호 조합을 생성)
            for left_string in self.generateParenthesis(left_count):
                # 오른쪽 부분 문자열 생성 (self.generateParenthesis(n - 1 - left_count): 오른쪽에 들어갈 괄호 조합을 생성)
                for right_string in self.generateParenthesis(n - 1 - left_count):
                    # 현재 조합을 결과 리스트에 추가
                    answer.append("(" + left_string + ")" + right_string)

        return answer

```

### Approach 4:
```py
```

### Approach 5:
```py
```