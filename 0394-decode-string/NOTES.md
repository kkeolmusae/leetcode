# 풀이
- LeetCode 75, Medium
- Stack
- Time: timeover
- 어려웠음. 처음에 재귀로 풀려다가 안풀려서 for로 바꿨다가 30분 넘어감. 

## 내 풀이
코드 자체는 어렵지 않음. 
```py
class Solution:
    def decodeString(self, s: str) -> str:
        q = []

        for st in s:
            if st == "]":  # 닫는 문자일때
                temp = ""
                while q and q[-1] != "[":  # 열린 문자가 나올때까지
                    temp = q.pop() + temp

                q.pop()  # 열린 문자삭제

                nums = ""

                while q and q[-1].isdigit():  # 숫자처리. 숫자가 한글자가 아닐 수 있음
                    nums = q.pop() + nums

                q.append(int(nums) * temp)
            else:
                q.append(st)

        return "".join(q)
```

## 다른 풀이
### Approach 1: Using Stack
내 코드랑 비슷한데 숫자 계산하는 부분이 다르고 문자 계산하는 부분에서 reverse를 씀
```py
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i] == ']':
                decoded_string = []
                # 스택에서 '['가 나올 때까지 문자를 빼서 decoded_string에 추가
                while stack and stack[-1] != '[':
                    decoded_string.append(stack.pop())
                
                # 스택에서 '['를 제거
                stack.pop()
                
                # 스택에서 숫자를 가져와서 k를 계산
                base = 1
                k = 0
                while stack and stack[-1].isdigit():
                    k = k + int(stack.pop()) * base
                    base *= 10
                
                # decoded_string을 k번 반복하여 스택에 다시 넣음
                decoded_string = decoded_string[::-1]  # 문자열을 뒤집기
                for _ in range(k):
                    stack.extend(decoded_string)
            else:
                # 현재 문자를 스택에 추가
                stack.append(s[i])
        
        # 스택에 남아 있는 문자를 합쳐서 결과 반환
        return "".join(stack)

```

### Approach 2: Using 2 Stack
숫자용 스택이랑 문자용 스택으로 나눠서 처리하는 방법
```py
class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        string_stack = []
        current_string = []
        k = 0
        
        for ch in s:
            if ch.isdigit():
                # 현재 숫자 계산 (예: '23'을 처리할 때 2*10 + 3)
                k = k * 10 + int(ch)
            elif ch == '[':
                # 현재까지 계산된 숫자와 문자열을 스택에 저장
                count_stack.append(k)
                string_stack.append(current_string)
                # 새로운 문자열과 숫자를 준비
                current_string = []
                k = 0
            elif ch == ']':
                # 스택에서 이전 문자열을 가져옴
                decoded_string = string_stack.pop()
                current_k = count_stack.pop()
                # 현재 문자열을 current_k 번 반복하여 이전 문자열에 추가
                decoded_string.extend(current_string * current_k)
                current_string = decoded_string
            else:
                # 문자라면 현재 문자열에 추가
                current_string.append(ch)
        
        # 모든 문자를 합쳐서 결과 반환
        return ''.join(current_string)

```

### Approach 3: Using Recursion

```py
class Solution:
    def __init__(self):
        self.index = 0  # 현재 처리중인 위치

    def decodeString(self, s: str) -> str:
        result = []
        
        while self.index < len(s) and s[self.index] != ']':
            if not s[self.index].isdigit():
                # 숫자가 아니면 바로 결과에 추가
                result.append(s[self.index])
                self.index += 1
            else:
                k = 0
                # 숫자를 모두 읽어서 k를 계산
                while self.index < len(s) and s[self.index].isdigit():
                    k = k * 10 + int(s[self.index])
                    self.index += 1
                # 여는 괄호 '['를 넘김
                self.index += 1
                # 재귀적으로 디코딩된 문자열을 얻음
                decoded_string = self.decodeString(s)
                # 닫는 괄호 ']'를 넘김
                self.index += 1
                # k[decoded_string]을 반복해서 결과에 추가
                result.append(decoded_string * k)
        
        return ''.join(result)

```