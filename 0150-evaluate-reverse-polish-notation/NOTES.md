# 풀이
- Difficulty:  Medium
- Topic:  Stack
- Elapsed Time:  10m
- Status:  O
- Memo:  문제 구현은 어렵지 않았는데 나눗셈 조건에서 "0에 가깝게 처리" 한다는 부분에서 시간을 절반 이상 사용했다.

## 내 풀이
문제 자체는 아주 쉬
```py
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = ["+", "-", "*", "/"]
        stack = []

        for token in tokens:
            if token in operator:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                  # 나눗셈 결과를 int 로 변환하는 방법으로 0에 가깝게 처리함
                    stack.append(
                        int(a / b),
                    )
            else:
                stack.append(int(token))
        return int(stack[0])
```

## 다른 풀이
### Approach 1: Reducing the List In-place
파이썬의 람다를 사용해서 tokens 를 줄이는 방법으로 해결함
```py
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 연산자에 대한 동작을 정의하는 딕셔너리
        operations = {
            "+": lambda a, b: a + b,  # 덧셈
            "-": lambda a, b: a - b,  # 뺄셈
            "/": lambda a, b: int(a / b),  # 나눗셈 (0 방향으로 소수점 버림)
            "*": lambda a, b: a * b,  # 곱셈
        }

        current_position = 0  # 현재 처리 중인 위치를 나타내는 포인터

        # 토큰 리스트가 하나의 요소만 남을 때까지 반복
        while len(tokens) > 1:

            # 현재 위치를 연산자가 있는 위치로 이동
            while tokens[current_position] not in "+-*/":
                current_position += 1

            # 연산자와 피연산자를 추출
            operator = tokens[current_position]  # 현재 연산자
            number_1 = int(tokens[current_position - 2])  # 첫 번째 숫자
            number_2 = int(tokens[current_position - 1])  # 두 번째 숫자

            # 연산자를 기반으로 결과를 계산
            operation = operations[operator]
            tokens[current_position] = operation(number_1, number_2)

            # 계산이 완료된 두 숫자를 제거하고, 연산 결과는 그대로 둠
            tokens.pop(current_position - 2)  # 첫 번째 숫자 제거
            tokens.pop(current_position - 2)  # 두 번째 숫자 제거
            current_position -= 1  # 포인터를 새 숫자 위치로 이동

        # 최종 결과를 정수로 반환
        return int(tokens[0])

```

### Approach 2: Evaluate with Stack
내 코드랑 거의 비슷함
```py
# 람다 사용
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b,
        }

        stack = []
        for token in tokens:
            if token in operations:
                number_2 = stack.pop()
                number_1 = stack.pop()
                operation = operations[token]
                stack.append(operation(number_1, number_2))
            else:
                stack.append(int(token))
        return stack.pop()

# 람다 미사용
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-/*":
                stack.append(int(token))
                continue

            number_2 = stack.pop()
            number_1 = stack.pop()

            result = 0
            if token == "+":
                result = number_1 + number_2
            elif token == "-":
                result = number_1 - number_2
            elif token == "*":
                result = number_1 * number_2
            else:
                result = int(number_1 / number_2)

            stack.append(result)

        return stack.pop()
```

### Approach 3:
```py
```

### Approach 4:
```py
```

### Approach 5:
```py
```