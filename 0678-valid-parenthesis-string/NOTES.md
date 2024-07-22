# 다른 풀이
문제 유형: DP, Stack, Greedy 

### 내 코드
- 이거 처음에 stack 두개 써서 문자 넣고, ")" 들어오면 "(" pop, 아니면 "*" pop 하는식으로 했음.
- 그랬는데 테스트케이스에서 몇개 실패해서 gpt 써서 원인 찾음.
- ")" 가 들어왔을때 "(" 에서 우선 pop하고 "*" 에서 pop 하는것 까지는 맞았는데
- "(" stack 이랑 "*" stack이랑 남았을때 나머지 처리하는 부분에서 틀렸던거임
- 만약 남은게 `((**` 이면 문제 없는데 `**((` 이면 문제가 되는거였음.
- 그래서 문자를 넣는게 아니라 idx를 넣어서 그걸로 확인해서 처리함

시간복잡도: O(n)

```py
class Solution:
    def checkValidString(self, s: str) -> bool:
        parenthesis = []
        stars = []
        for idx, st in enumerate(s):
            if st == "(":
                parenthesis.append(idx)
            elif st == "*":
                stars.append(idx)
            else:
                if len(parenthesis):
                    parenthesis.pop()
                elif len(stars):
                    stars.pop()
                else:
                    return False
        while len(parenthesis) and len(stars):
            # 마지막 "(" 가 마지막 "*" 보다 인덱스가 크면(더 뒤에 있으면) pop 못하는거라 False
            if parenthesis[-1] > stars[-1]:
                return False
            parenthesis.pop()
            stars.pop()

        return not parenthesis  # "(" 가 있으면 False, 없으면 True
```

### DP (Top Down) 로 푼 경우

시간복잡도: O(n*n)
```py
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        memo = [[-1] * n for _ in range(n)]  # n * n 의 memo
        return self.is_valid_string(0, 0, s, memo)

    def is_valid_string(
        self, index: int, open_count: int, s: str, memo: List[List[int]]
    ) -> bool:
        # 문자열의 끝에 도달한 경우 (index == len(s)), 모든 열린 괄호가 닫혔는지 (open_count == 0)를 확인합니다. 그렇다면 True를 반환하고, 그렇지 않으면 False를 반환합니다
        if index == len(s):
            return open_count == 0

        # 이미 계산된 결과가 있으면 (memo[index][open_count] != -1) 해당 결과를 반환합니다
        if memo[index][open_count] != -1:
            return memo[index][open_count] == 1

        is_valid = False
        # *는 (, ), 또는 빈 문자열로 처리될 수 있습니다. is_valid_string 함수를 호출하여 *가 각각 (, ), 빈 문자열로 처리될 때의 결과를 확인합니다.
        # |= 연산자를 사용하여 여러 가능성 중 하나라도 True이면 is_valid가 True가 됩니다
        if s[index] == "*":
            # (는 열린 괄호의 수를 증가시킵니다.
            is_valid |= self.is_valid_string(index + 1, open_count + 1, s, memo)
            if open_count > 0:
                # )는 열린 괄호의 수를 감소시킵니다 (단, 열린 괄호의 수가 0보다 큰 경우에만).
                is_valid |= self.is_valid_string(index + 1, open_count - 1, s, memo)
            # Treat '*' as empty
            is_valid |= self.is_valid_string(index + 1, open_count, s, memo)
        else:
            # Handle '(' and ')'
            if s[index] == "(":
                # Increment count for '('
                is_valid = self.is_valid_string(index + 1, open_count + 1, s, memo)
            elif open_count > 0:
                # Decrement count for ')'
                is_valid = self.is_valid_string(index + 1, open_count - 1, s, memo)

        # is_valid 값을 memo 배열에 저장하여, 이후 동일한 인덱스와 열린 괄호 수에 대해 재계산하지 않도록 합니다.
        memo[index][open_count] = 1 if is_valid else 0
        return is_valid
```

### DP (Bottom Up) 
시간복잡도: O(n)
```py
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        # dp[i][j] represents if the substring starting from index i is valid with j opening brackets
        dp = [[False] * (n + 1) for _ in range(n + 1)]

        # base case: an empty string with 0 opening brackets is valid
        dp[n][0] = True

        for index in range(n - 1, -1, -1):
            for open_bracket in range(n):
                is_valid = False

                # '*' can represent '(' or ')' or '' (empty)
                if s[index] == '*':
                    if open_bracket < n:
                        is_valid |= dp[index + 1][open_bracket + 1]  # try '*' as '('
                    # opening brackets to use '*' as ')'
                    if open_bracket > 0:
                        is_valid |= dp[index + 1][open_bracket - 1]  # try '*' as ')'
                    is_valid |= dp[index + 1][open_bracket]  # ignore '*'
                else:
                    # If the character is not '*', it can be '(' or ')'
                    if s[index] == '(':
                        is_valid |= dp[index + 1][open_bracket + 1]  # try '('
                    elif open_bracket > 0:
                        is_valid |= dp[index + 1][open_bracket - 1]  # try ')'
                dp[index][open_bracket] = is_valid

        return dp[0][0]  # check if the entire string is valid with no excess opening brackets
```

### Two Pointer 
시간 복잡도: O(n) / 공간 복잡도: O(1) 
양 끝에서 탐색함. 
- 문자열을 앞뒤로 동시에 탐색하며 여는 괄호와 닫는 괄호의 균형을 유지하려고 함
- open_count는 왼쪽부터 시작하여 여는 괄호 ( 또는 별표 *를 추적함
- close_count는 오른쪽부터 시작하여 닫는 괄호 ) 또는 별표 *를 추적함
- 각 위치에서 여는 괄호와 닫는 괄호의 수가 모두 음수가 되지 않도록 함

```py
class Solution:
    def checkValidString(self, s: str) -> bool:
        open_count = 0
        close_count = 0
        length = len(s) - 1
        
        # Traverse the string from both ends simultaneously
        for i in range(length + 1):
            # Count open parentheses or asterisks
            if s[i] == '(' or s[i] == '*':
                open_count += 1
            else:
                open_count -= 1
            
            # Count close parentheses or asterisks
            if s[length - i] == ')' or s[length - i] == '*':
                close_count += 1
            else:
                close_count -= 1
            
            # If at any point open count or close count goes negative, the string is invalid
            if open_count < 0 or close_count < 0:
                return False
        
        # If open count and close count are both non-negative, the string is valid
        return True
```