​# 풀이
- Difficulty:  Easy
- Topic:  Stack
- Elapsed Time:  3m
- Status:  O (2 times)
- Memo:  쉬웠음

## 내 풀이
```py
class Solution:
    def isValid(self, s: str) -> bool:
        open = ["(", "[", "{"]
        close = [")", "]", "}"]
        if len(s) == 1:
            return False

        q = []
        for st in s:
            if st in open:
                q.append(st)
            else:
                if not q:
                    return False
                op = q.pop()
                if op == open[0] and st != close[0]:
                    return False
                if op == open[1] and st != close[1]:
                    return False
                if op == open[2] and st != close[2]:
                    return False

        return True if not q else False
```

## 다른 풀이
### Approach 1: Stacks
아주 쉽게 풀었다
```py
class Solution(object):
    def isValid(self, s: str) -> bool:

        stack = []

        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"

                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
```

### Approach 2:
```py
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