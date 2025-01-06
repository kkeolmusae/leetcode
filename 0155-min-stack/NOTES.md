# 풀이
- Difficulty:  Medium
- Topic:  Stack
- Elapsed Time:  10m
- Status:  O
- Memo:  배열(Stack)을 두개를 쓰자는 접근법만 생각해내면 금방 푸는 문제였다.

## 내 풀이
```py
class MinStack:

    def __init__(self) -> None:
        self.min_stack = []
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:  # 최소값이 들어왔으면
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.min_stack[-1] == self.stack[-1]:  # 최소값이 양쪽에 있는거니깐
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

## 다른 풀이
### Approach 1: Stack of Value/ Minimum Pairs
현재값과 최소값을 튜플형태로 하나의 스택에 저장해서 처리하는 방법
```py
class MinStack:

    def __init__(self):
        # 스택을 저장할 리스트를 초기화합니다.
        self.stack = []

    def push(self, x: int) -> None:
        # 스택이 비어 있는 경우, 현재 값이 최소값이 됩니다.
        if not self.stack:
            self.stack.append((x, x))  # (현재 값, 최소값)을 튜플로 저장
            return

        # 스택의 마지막 요소의 최소값을 가져옵니다.
        current_min = self.stack[-1][1]
        # 현재 값과 이전 최소값 중 더 작은 값을 최소값으로 저장합니다.
        self.stack.append((x, min(x, current_min)))

    def pop(self) -> None:
        # 스택에서 가장 마지막 요소를 제거합니다.
        self.stack.pop()

    def top(self) -> int:
        # 스택의 가장 위에 있는 값을 반환합니다.
        return self.stack[-1][0]

    def getMin(self) -> int:
        # 스택의 현재 최소값을 반환합니다.
        return self.stack[-1][1]

```

### Approach 2: Two Stacks
내 구현방법과 똑같다
```py
class MinStack:

    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

### Approach 3: Improved Two Stacks
- min_stack 에 최소값을 저장할 때 최소값과 함께 해당 숫자가 반복된 횟수를 같이 저장함
- `Approach 2` 에서는 동일한 최소값이 여러번 나오면 불필요한 반복을 하게 되는데 이를 방지한 방법임
```py
class MinStack:

    def __init__(self):
        # 일반 스택과 최소값을 관리할 스택을 각각 초기화합니다.
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        # 일반 스택에 값을 추가합니다.
        self.stack.append(x)

        # 최소값 스택이 비어 있거나 현재 값이 최소값 스택의 최상단 값보다 작은 경우,
        # 최소값 스택에 값을 추가하고 해당 값의 개수를 1로 설정합니다.
        if not self.min_stack or x < self.min_stack[-1][0]:
            self.min_stack.append([x, 1])

        # 현재 값이 최소값 스택의 최상단 값과 같은 경우, 해당 값의 개수를 증가시킵니다.
        elif x == self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1

    def pop(self) -> None:
        # 일반 스택의 최상단 값이 최소값 스택의 최상단 값과 같은 경우,
        # 최소값 스택의 개수를 1 감소시킵니다.
        if self.min_stack[-1][0] == self.stack[-1]:
            self.min_stack[-1][1] -= 1

        # 최소값 스택의 최상단 값의 개수가 0이 되면 해당 값을 제거합니다.
        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()

        # 일반 스택에서도 최상단 값을 제거합니다.
        self.stack.pop()

    def top(self) -> int:
        # 일반 스택의 최상단 값을 반환합니다.
        return self.stack[-1]

    def getMin(self) -> int:
        # 최소값 스택의 최상단 값을 반환합니다.
        return self.min_stack[-1][0]
```
